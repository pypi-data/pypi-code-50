Ans="""
'''

Name.html
<html>
<body bgcolor="blue">
<form action="http://192.168.8.3:8080/servlet/Greeting " method="get">
<input type="text" name="uname">
<input type="Submit" value="Submit">
<input type="Reset" value="Reset"></form>
</body>
</html>

Servlet File
Greeting.java



import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;
public class Greeting extends HttpServlet
{
public void doGet(HttpServletRequest req,HttpServletResponse res) throws ServletException,IOException
{
String username=req.getParameter("uname");
PrintWriter out=res.getWriter();
res.setContentType("text/html");
out.println("Welcome"+username);
out.close();
}
} 

'''
"""
