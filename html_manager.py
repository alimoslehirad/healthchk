import cherrypy
class Html_manager:

    @cherrypy.expose
    def create_index(self , request_list):
        index = open("indexformat.html").read().format(var1=request_list[0][0]+'       '+request_list[0][1],var2=request_list[1][0]+'      '+request_list[1][1],var3=request_list[2][0]+'       '+request_list[2][1],var4='goodbye',var5='goodbye',var6='goodbye')
        return index

    def write_index(self,request_list):
        new_index=self.create_index(request_list)
        f = open("index.html", "w")
        f.write(new_index)
        f.close()


