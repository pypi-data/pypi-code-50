Ans="""
'''

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class ServletLifeCycle extends HttpServlet
{
public ServletLifeCycle()
{
System.out.println(“Am from default constructor”);
}
public void init(ServletConfig config)
{
System.out.println(“Am from Init method…!”);
}
public void doGet(HttpServletReuest req, HttpServletResponse res)throws ServletException, IOException
{
 res.setContentType(“text/html”);
PrintWriter pw =  res.getWriter();
pw.println(“I am from doGet method”);
pw.close();
}
public void destroy()
{
System.out.println(“Am from Destroy methods”);
}
}


Web.xml

<web-app>
<servlet>
<servlet-name>second</servlet-name>
<servlet-class>java4s.ServletLifeCycle</servlet-class>
<load-on-startup>1</load-on-startup>
</servlet>

<servlet-mapping>
<servlet-name>second</servlet-name>
<url-pattern>/lifecycle1</url-pattern>
</servlet-mapping>
</web-app>


'''
"""
