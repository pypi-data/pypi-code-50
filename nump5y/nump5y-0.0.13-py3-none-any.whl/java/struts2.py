Ans="""
'''

Steps to create Struts Application –
Download and extract Struts2 binary distribution files. It is freely available online. Here it is recommend downloading the “Full Distribution” zip file containing all dependency jar files.
1.Create JSPs
2.Create action pages according to JSPs
3.Connect the JSPs ad action pages using configuration files (such as web.xml and struts.xml).
Web Application1
-Web pages
-Meta-INF Context.xml
-Web-INF Web.xml
-Source packages
-Default packages
-Libraries
-All struts libraries 
-Configuration files 
-Manifest.MF
-Context.xml
-Web-fragment.xml
-Web.xml

1.And create “index.jsp” by selecting new Java server page document.

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%taglib prefix = "s" uri="/struts-tags"%>
<html>
<body>
<s:form method ="post" action ="hello_action">
<s:labelvalue ="Enter your name in text box and click the button" name="label1"/>
<s:textfield name ="name"/>
<s:submit value ="CLICK" name="submit"/>
</s:form>
</body>
</html>
2.This will generate certain output.
3.Create another jsp page named as “result.jsp” inside jsp folder.

//result.jsp
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%taglib prefix = "s" uri="/struts-tags"%>
<html>
<body>
<h1>Hello<s:property value="name"/></h1>
</body>
</html>
4.The folder here is known as package. Create a folder named action_jsp inside source packages.
5.Create action class “hello_action” inside “action_jsp” package.
6.So the hello_action java file will be as follwos:

import com.opensymphony.xwork2.ActionSupport;
//everything in here must be kept public to have package level access.

public class hello_ation extends ActionSupport
{
private String name;
//getter and setter methods for the form element value
 public String getName()
{
return name;
}
public void setName(String name)
{
this.name = name;
}
//method that returns success or failure on action
public String execute()
{
return "success";
}
}
 
7.Struts.xml can be written as:

<!DOCTYPE struts PUBLIC
"-//Apache Software Foundation//DTD Sturts Configuration 2.0//En"
"http://struts.apache.org/dtds/struts-2.0.dtd">

<struts>
<package name ="default" extends ="struts-default">
<action name ="hello_action" class ="action_jsp.hello_action" method ="execute">
<result name ="success">result.jsp</result>
<result name ="failure">index.jsp</result>
</action>
</package>
</struts>
 
8.In web.xml, change the welcome file to our index.jsp

<?xml version ="1.0" encoding ="UTF-8"?>


<web-app version ="3.1" xmlns = "http://xmlns.jcp.org/xml/ns/javaee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
xsi:schemaLocation ="http://xmlns.jcp.org./xml/ns//javaee http://xmlns.jcp.org./xml/ns/javaee/web-app_3_1.xsd">
<filter>
<filter-name>struts2</filter-name>
<filter-class>org.apace.struts2.dispatcher.FilterDispatcer</filter-class>
</filter>
<filter-mapping>
<filter-name>struts<//filter-name>
<url-pattern>/*</url-pattern>
</filter-mapping>
<session-config>
<session-timeout>
30
</sesson-timeout>
</session-config>
<welcome-file-list>
<welcome-file>jsp/index.jsp</welcome-file>
</welcome-file-list>
</web-app>

9.Run the application. And see the welcome message.


'''
"""
