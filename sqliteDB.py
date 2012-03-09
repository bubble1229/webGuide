import sqlite3

g_urls_map = {}
g_groups  = []


def getConnection():
	conn = sqlite3.connect("links.db")
	conn.text_factory = str
	return conn

def doAddLink(gid, name, url, title):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("insert into `link` (`gid`, `name`, `url`, `title`) values (?, ?, ?, ?)" , (gid, name, url, title))
    conn.commit()
    conn.close()
    refreshMem()

def doAddGroup(gid, name):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("insert into `group` (`gid`, `name`) values (?, ?)" , (gid, name))
    conn.commit()
    conn.close()
    refreshMem()


def doUpdateLink(id, gid, name, url, title):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("update `link` set `name` = ?, `url` = ?, `title` = ? where `id` = ? and `gid` = ?", (name, url, title, id, gid))
    conn.commit()
    conn.close()
    refreshMem()

def doUpGroup(id, gid, name):
    conn = getConnection()
    cursor = conn.cursor()
    print("update `group` set `name` = ? where `id` = ? and `gid` = ?")
    cursor.execute("update `group` set `name` = ? where `id` = ? and `gid` = ?", (name, id, gid))
    conn.commit()
    conn.close()
    refreshMem()


def doDelete(id, gid):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("delete from `link`  where `id` = ? and `gid` = ?", (id, gid))
    conn.commit()
    conn.close()
    refreshMem()

def doDelGroup(id, gid):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("delete from `group`  where `id` = ? and `gid` = ?", (id, gid))
    conn.commit()
    conn.close()
    refreshMem()
        

def getHttpUrls(gid):
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("select `url`,`title`,`name`,`gid`,`id` from `link` where `gid` = ? order by id asc", (gid,))
    return cursor.fetchall()

def getAllHttpUrls():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("select `url`,`title`,`name`,`gid`,`id` from `link` order by id asc")
    return cursor.fetchall()
    
def getAllGid():
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute("select `name`,`gid`,`id` from `group` order by gid asc")
    return cursor.fetchall()


def getAllUrlsMap(groups):

    urls_map = {}
    for gid in groups:
        tmpMap = {}
        tmpMap[gid[0]] = getHttpUrls(gid[1])
        urls_map[gid[1]] = tmpMap
    return urls_map



def refreshMem():
    global g_groups
    global g_urls_map
    groups = getAllGid()
    urls_map = getAllUrlsMap(groups)
    g_urls_map = urls_map
    g_groups = groups


