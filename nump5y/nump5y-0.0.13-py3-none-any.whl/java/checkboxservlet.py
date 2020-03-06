Ans="""
'''

index.jsp

<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Check Box Test</title>
</head>
<body>
<form action="checkBoxData" method="post">
<table>
<tr>
<td>
<input type="checkbox" name="hobbies" value="Singing">Singing
</td>
</tr>
<tr>
<td>
<input type="checkbox" name="hobbies" value="Dancing">Dancing
</td>
</tr>
<tr>
<td>
<input type="checkbox" name="hobbies" value="Painting">Painting
</td>
</tr> 
<tr>
<td>
<input type="submit" value="Send">
</td>
</tr>
</table>
</form>
</body>
</html>

CheckBoxDemoServlet.java

package CheckBoxDemo;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class CheckBoxDemoServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doPost(request,response);
    }
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    try
    {
     String hobbise[] = request.getParameterValues("hobbies") ;
     
     PrintWriter writer =  response.getWriter();
     response.setContentType("text/html");
     writer.println("<h2><font color=green>Your Hobbies :</font></h2>");
     
     for(String value : hobbise)
     {
     writer.println("<br><font color=blue>"+value+"</font>");
     }  
     
     writer.close();
    }
    catch(Exception exception)
    {
        exception.printStackTrace();    
    }
    }
}

web.xml

 <?xml version="1.0" encoding="UTF-8"?>
<web-app xmlns:web="http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd">
  <servlet>
    <servlet-name>checkBoxServlet</servlet-name>
    <servlet-class>CheckBoxDemo.CheckBoxDemoServlet</servlet-class>
  </servlet>
  <servlet-mapping>
    <servlet-name>checkBoxServlet</servlet-name>
    <url-pattern>/checkBoxData</url-pattern>
  </servlet-mapping>
  <welcome-file-list>
    <welcome-file>index.jsp</welcome-file>
  </welcome-file-list>
</web-app>

'''
"""
