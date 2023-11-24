from flask import Flask
from pyhtml import *
from web.home import home

class UI_View(Tag):
    def __init__(self, *args, **kwargs):
        super().__init__("test", *args, **kwargs)

app = Flask(
    __name__,
    template_folder='',
    static_folder='web'
)

@app.route('/')
def index():
    t = html(
            head(
            meta(charset="utf-8"),
            meta(name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no"),
            meta(name="google", content="notranslate"),
            link(rel="shortcut icon", href="/lib/web/favicon.ico", type="image/x-icon"),
            script(src="https://unpkg.com/event-target-shim@6.0.2"),
            script(src="//unpkg.com/alpinejs"),
            script(src="https://cdn.jsdelivr.net/npm/@uirouter/core@6.1.0/_bundles/ui-router-core.js"),
            script("""
                window.app = {};
                let EventTarget = EventTargetShim.EventTarget;
            """),
            link(rel="stylesheet", href="{{url_for('static', filename='app.css')}}")
        ),
        body(
            nav(id="main-layout")(
                ul(
                    li(
                        a(href="./")("FLX")
                    )
                ),                
            ),
            script(
                """
                if (window.location.hostname == "localhost") {
                    // TODO move port to env
                    document.write("<script async src='http://HOST:3000/browser-sync/browser-sync-client.js?v=2.27.10'><\/script>".replace("HOST", location.hostname));
                }
                """
            ),
            script(
                type="module",
                src="{{url_for('static', filename='app.js')}}"
            ),
            UI_View()
        )
    )
    return t.render()

app.register_blueprint(home.home)

if __name__ == '__main__':
    app.run()