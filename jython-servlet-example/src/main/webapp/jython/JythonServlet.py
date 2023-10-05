from javax.servlet.http import HttpServlet

class JythonServlet (HttpServlet):

    def doGet(self,request,response):
        print("JythonServlet doGet executed ")
        self.doWork (request,response)

    def doPost(self,request,response):
        print("JythonServlet doPost executed ")
        self.doWork (request,response)

    def doWork(self,requst,response):
        print("JythonServlet doWork executed ")
        requst.setAttribute("msg", "Hello  " + requst.getParameter("userName"));
        requst.getRequestDispatcher("/myJsp").forward(requst, response);