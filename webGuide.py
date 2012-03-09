import web
import sqliteDB as db



urls = (
    '/(.*)/', 'redirect',
    '/', 'index',
    '/index', 'index',
    '/elink', 'elink',
    '/upGroup', 'upGroup',
    '/updateLink', 'updateLink',
    '/addGroup', 'addGroup',
    '/addLink', 'addLink',
    '/delete', 'delete',
    '/delGroup', 'delGroup',
    '/refresh','refresh'    
)


app = web.application(urls, globals())
render = web.template.render('templates/')

if __name__ == "__main__":
	app.run()

db.refreshMem()


class index: 
    def GET(self):
        urls = db.g_urls_map 
        print(urls)
        params = web.Storage(locals())
        return render.index(params)


class elink:
    def GET(self):
        urls = db.getAllHttpUrls()
        groups = db.g_groups
        params = web.Storage(locals())
        return render.elink(params)

class delGroup:
    def POST(self):
        params = web.input()
        db.doDelGroup(params.id.strip(), params.gid.strip())

class delete:
    def POST(self):
        params = web.input()
        db.doDelete(params.id, params.gid)

class addGroup:
    def POST(self):
        params = web.input()
        print('##########')
        print(params)
        db.doAddGroup(params.gid.strip(), params.name.encode('utf-8').strip())

class addLink:
    def POST(self):
        params = web.input()
        db.doAddLink(params.gid.strip(), params.name.encode('utf-8').strip(), 
        params.url.encode('utf-8').strip(), params.title.encode('utf-8').strip())

class upGroup:
    def POST(self):
        params = web.input()
        db.doUpGroup(params.id.strip(), params.gid.strip(), params.name.encode('utf-8').strip())

class updateLink:
    def POST(self):
        params = web.input()
        db.doUpdateLink(params.id.strip(), params.gid, params.name.encode('utf-8').strip(), 
        params.url.encode('utf-8').strip(), params.title.encode('utf-8').strip())


class refresh:
    def POST(self):
        db.refreshMem()
