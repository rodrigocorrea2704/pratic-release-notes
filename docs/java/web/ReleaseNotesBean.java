package br.com.sercod.pratic.view;

import javax.faces.bean.ManagedBean;
import javax.faces.bean.RequestScoped;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.Serializable;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.stream.Collectors;

import com.vladsch.flexmark.html.HtmlRenderer;
import com.vladsch.flexmark.parser.Parser;
import com.vladsch.flexmark.util.ast.Node;
import com.vladsch.flexmark.util.data.MutableDataSet;

@ManagedBean(name = "releaseNotesBean")
@RequestScoped
public class ReleaseNotesBean implements Serializable {

    private static final String RAW_URL =
        "https://raw.githubusercontent.com/rodrigocorrea2704/pratic-release-notes/main/release-notes/notas_latest.md";

    private String notasHtml;
    private String erro;

    public void carregarNotas() {
        try {
            String markdown = buscarMarkdown(RAW_URL);
            notasHtml = converterParaHtml(markdown);
        } catch (Exception e) {
            erro = "Não foi possível carregar as notas de alterações.";
        }
    }

    private String buscarMarkdown(String urlStr) throws Exception {
        URL url = new URL(urlStr);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        conn.setConnectTimeout(5000);
        conn.setReadTimeout(10000);
        conn.setRequestProperty("Accept", "text/plain");

        try (BufferedReader reader = new BufferedReader(
                new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8))) {
            return reader.lines().collect(Collectors.joining("\n"));
        }
    }

    private String converterParaHtml(String markdown) {
        MutableDataSet options = new MutableDataSet();
        Parser parser = Parser.builder(options).build();
        HtmlRenderer renderer = HtmlRenderer.builder(options).build();
        Node document = parser.parse(markdown);
        return renderer.render(document);
    }

    public String getNotasHtml() { return notasHtml; }
    public String getErro()      { return erro; }
}
