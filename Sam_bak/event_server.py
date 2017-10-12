import web
from sam_event_handling import key_event


urls = ("/", "index")
app = web.application(urls, globals())
render = web.template.render('templates/')

class index:
    def GET(self):
        #print("test")
        arbitraryvariable = None
        return render.index(arbitraryvariable)

#class EventHandling:
    def POST(self):
        keystroke = web.data()
        # Run Sams code handling
        key_event(keystroke)

if __name__ == "__main__":
    app.run()
