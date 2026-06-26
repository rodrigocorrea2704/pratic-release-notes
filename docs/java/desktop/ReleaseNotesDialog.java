package br.com.sercod.pratic.ui;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.stream.Collectors;

/**
 * Exibe as notas de alterações do Pratic RH buscadas do GitHub.
 * Uso: ReleaseNotesDialog.exibir(parentFrame);
 */
public class ReleaseNotesDialog extends JDialog {

    private static final String RAW_URL =
        "https://raw.githubusercontent.com/rodrigocorrea2704/pratic-release-notes/main/release-notes/notas_latest.md";

    private ReleaseNotesDialog(Frame parent) {
        super(parent, "Novidades — Pratic RH", true);
        setSize(760, 560);
        setLocationRelativeTo(parent);
        setLayout(new BorderLayout(8, 8));

        JEditorPane editor = new JEditorPane();
        editor.setEditable(false);
        editor.setContentType("text/html");
        editor.putClientProperty(JEditorPane.HONOR_DISPLAY_PROPERTIES, true);
        editor.setFont(new Font("SansSerif", Font.PLAIN, 13));

        JScrollPane scroll = new JScrollPane(editor);
        add(scroll, BorderLayout.CENTER);

        JButton fechar = new JButton("Fechar");
        fechar.addActionListener((ActionEvent e) -> dispose());
        JPanel rodape = new JPanel(new FlowLayout(FlowLayout.RIGHT));
        rodape.add(fechar);
        add(rodape, BorderLayout.SOUTH);

        // carrega em background para não travar a UI
        SwingWorker<String, Void> worker = new SwingWorker<String, Void>() {
            @Override
            protected String doInBackground() throws Exception {
                String md = buscarMarkdown(RAW_URL);
                return markdownParaHtml(md);
            }
            @Override
            protected void done() {
                try {
                    editor.setText(get());
                    editor.setCaretPosition(0);
                } catch (Exception ex) {
                    editor.setContentType("text/plain");
                    editor.setText("Não foi possível carregar as notas de alterações.\n" + ex.getMessage());
                }
            }
        };
        worker.execute();
    }

    // ------------------------------------------------------------------ //

    private static String buscarMarkdown(String urlStr) throws Exception {
        URL url = new URL(urlStr);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        conn.setConnectTimeout(5000);
        conn.setReadTimeout(10000);
        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
            return reader.lines().collect(Collectors.joining("\n"));
        }
    }

    /**
     * Conversão Markdown → HTML simplificada, sem dependência externa.
     * Suporta: # h1/h2, **negrito**, listas, ---  e quebras de linha.
     */
    private static String markdownParaHtml(String md) {
        StringBuilder sb = new StringBuilder();
        sb.append("<html><body style='font-family:sans-serif;font-size:13px;margin:12px'>");
        for (String linha : md.split("\n")) {
            if (linha.startsWith("# ")) {
                sb.append("<h2 style='color:#2c3e50'>").append(esc(linha.substring(2))).append("</h2>");
            } else if (linha.startsWith("## ") || linha.startsWith("🗂️")) {
                sb.append("<h3 style='color:#34495e;margin-top:14px'>").append(esc(linha)).append("</h3>");
            } else if (linha.startsWith("---")) {
                sb.append("<hr/>");
            } else if (linha.startsWith("✅") || linha.startsWith("🔧") || linha.startsWith("🆕")) {
                sb.append("<p style='margin:6px 0'><b>").append(esc(linha)).append("</b></p>");
            } else if (linha.trim().isEmpty()) {
                sb.append("<br/>");
            } else {
                // negrito inline **texto**
                String html = esc(linha).replaceAll("\\*\\*(.+?)\\*\\*", "<b>$1</b>");
                sb.append("<p style='margin:2px 0 2px 8px'>").append(html).append("</p>");
            }
        }
        sb.append("</body></html>");
        return sb.toString();
    }

    private static String esc(String s) {
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;");
    }

    // ------------------------------------------------------------------ //

    /** Ponto de entrada para abrir o dialog a partir de qualquer tela. */
    public static void exibir(Frame parent) {
        new ReleaseNotesDialog(parent).setVisible(true);
    }
}
