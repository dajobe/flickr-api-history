from __future__ import annotations

from flickr_api_history.check_method_doc import main, method_doc_lines


def method_page(method: str, body: str) -> str:
    return f"""
    <html>
      <head>
        <title>Flickr Services: Flickr API: {method}</title>
        <script>ignored();</script>
      </head>
      <body>
        <nav>Navigation should be ignored by the start marker.</nav>
        <h1>{method}</h1>
        {body}
        <h3>API Explorer</h3>
        <p>This text is outside the method documentation body.</p>
      </body>
    </html>
    """


def test_method_doc_lines_extracts_method_body() -> None:
    html = method_page(
        "flickr.photos.search",
        """
        <p>Return a list of photos matching some criteria.</p>
        <h3>Arguments</h3>
        <dl>
          <dt>api_key</dt>
          <dd>Your API application key.</dd>
        </dl>
        """,
    )

    assert method_doc_lines(html, "flickr.photos.search") == [
        "flickr.photos.search",
        "Return a list of photos matching some criteria.",
        "Arguments",
        "api_key",
        "Your API application key.",
    ]


def test_main_reports_no_change_for_same_document(tmp_path, capsys) -> None:
    archive = tmp_path / "flickr.photos.search.html"
    fetched = tmp_path / "flickr.photos.search.html.new"
    archive.write_text(
        method_page("flickr.photos.search", "<p>Same documentation.</p>"),
        encoding="utf-8",
    )

    result = main(
        [
            "--method",
            "flickr.photos.search",
            "--archive",
            str(archive),
            "--url",
            archive.as_uri(),
            "--fetched-output",
            str(fetched),
        ]
    )

    assert result == 0
    assert not fetched.exists()
    assert "No change in flickr.photos.search documentation" in capsys.readouterr().out


def test_main_writes_fetched_html_and_diff_for_changed_document(
    tmp_path, capsys
) -> None:
    archive = tmp_path / "flickr.photos.search.html"
    current = tmp_path / "current.html"
    fetched = tmp_path / "flickr.photos.search.html.new"
    archive.write_text(
        method_page("flickr.photos.search", "<p>Old documentation.</p>"),
        encoding="utf-8",
    )
    current_html = method_page("flickr.photos.search", "<p>New documentation.</p>")
    current.write_text(current_html, encoding="utf-8")

    result = main(
        [
            "--method",
            "flickr.photos.search",
            "--archive",
            str(archive),
            "--url",
            current.as_uri(),
            "--fetched-output",
            str(fetched),
        ]
    )

    output = capsys.readouterr().out
    assert result == 1
    assert fetched.read_text(encoding="utf-8") == current_html
    assert "-Old documentation." in output
    assert "+New documentation." in output
