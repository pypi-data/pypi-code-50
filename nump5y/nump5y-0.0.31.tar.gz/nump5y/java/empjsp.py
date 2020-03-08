Ans="""
'''

Index.jsp

<!DOCTYPE html>
<html>
<head>
<meta http-euiv="Content-Type" content="text/html";charset=ISO-8859-1">
<title>JSP CRUD Example</title>
</head>
<body>
<h1>JSP CRUD Example</h1>
<a href="adduserform.jsp">Add User</a>
<a href="viewuser.jsp">View Users</a>
</body>
</html>

Adduserform.jsp

<!DOCTYPE html>
<html>
<head>
<meta http-euiv="Content-Type" content="text/html";charset=ISO-8859-1">
<title>JSP CRUD Example</title>
</head>
<body>

<jsp:include page="userform.html"></jsp:include>
</body>
</html>
Userform.html
0<a href="viewusers.jsp">View All Records</a><br/>
<h1>Add New User</h1>
<form action="adduser.jsp" method="post">
<table>
<tr><td>Name:</td><td><input type="text" name="name"/></td></tr>
<tr><td>Password:</td><td><input type="password" name="password"/></td></tr>
<tr><td>Email:</td><td><input type='"email" name="email"/></td></tr>
<tr><td>Sex:</td><td>
<input type="radio" name="sex" value"male"/>Male
<input type="radio" name="sex" value"female"/>Female</td></tr>
<tr><td>Country:</td><td>
<select name='country' style='width:150px'>
<option>India</option>
<option>Pakistan</option>
<option>Afghanistan</option>
<option>Berma</option>
<option>Other</option>
</select>
</td></tr>
<tr><td colspan='2'><input type="submit" value="Add User"/></td></tr>
</table>
</form>

Adduser.jsp

<%@page import="com.javapoint.dao.UserDao"%>
<jsp:useBean id="u" class="com.javapoint.bean.User"></jsp:useBean>
<jsp:setProperty property="*" name="u"/>

<%
int i=UserDao.save(u);
if(i>0)
{
response.sendRedirect("adduser-success.jsp");
}
else
{
response.sendRedirect("adduser-error.jsp");
}
%>

User.java

package com.javapoint.bean;
public class User
{
private int id;
private String name,password,emai,sex,country;
}

UserDao.java

package com.javapoint.dao;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import com.javapoint.bean.User;
public class UserDao
{
public static Connection getConnection()
{
Connection con=null;
try
{
Class.forName("com.mysql.jdbc.Driver");
con=DriverManager.getConnection("jdbc:mysql://localhost:3306/test","","");
}
catch(Exception e)
{
System.out.println(e);
}
return con;
}

public static int save(User u)
{
int status=0;
try
{
Connection con = getConnection();
PreparedStatement ps = con.prepareStatement("insert into register(name,password,email,sex,country) values(?,?,?,?,?)");
ps.setString(1,u.getName()); 
ps.setString(2,u.getPassword());
ps.setString(3,u.getEmail());
ps.setString(4,u.getSex());
ps.setString(5,u.getCountry()); 
status=ps.executeUpdate();
}
catch(Exception e)
{
System.out.println(e);
}
return status;
}
public static int update(User u)
{
int status=0;
try
{
Connection con = getConnection();
PreparedStatement ps = con.prepareStatement("update register set name=?,password=?,email=?,sex=?,country=? where id =?");
ps.setString(1,u.getName()); 
ps.setString(2,u.getPassword());
ps.setString(3,u.getEmail());
ps.setString(4,u.getSex());
ps.setString(5,u.getCountry());
ps.setInt(6,u.getId()); 
status=ps.executeUpdate();
}
catch(Exception e)
{
System.out.println(e);
}
return status;
}
public static int delete(User u)
{
int status=0;
try
{
Connection con = getConnection();
PreparedStatement ps = con.prepareStatement("insert into register(name,password,email,sex,country) values(?,?,?,?,?)");
ps.setInt(6,u.getId()); 
status=ps.executeUpdate();
}
catch(Exception e)
{
System.out.println(e);
}
return status;
}

public static List<User> getAllRecords()
{
List<User> list = new ArayList<User>();
try
{
Connection con = getConnection();
PreparedStatement ps = con.prepareStatement("select * from register");
ResultSet rs = ps.executeQuery();
while(rs.next())
{
User u = new User();
u.setId(rs.getInt("id"));
u.setName(rs.getString("name"));
u.setPassword(rs.getString("password"));
u.setEmail(rs.getString("email"));
u.setSex(rs.getString("sex"));
u.setCountry(rs.getString("country"));
list.add(u);
}
catch(Exception e)
{
System.out.println(e);
}
return list;
}
public static User getRecordById(int id)
{
User u = null;
try
{
Connection con = getConnection();
PreparedStatement ps = con.prepareStatement("select * from register where id=?");
ps.setInt(1,id);
ResultSet rs = ps.executeQuery();
while(rs.next())
{
u = new User();
u.setId(rs.getInt("id"));
u.setName(rs.getString("name"));
u.setPassword(rs.getString("password"));
u.setEmail(rs.getString("email"));
u.setSex(rs.getString("sex"));
u.setCountry(rs.getString("country"));
}
catch(Exception e)
{
System.out.println(e);
}
return u;
}
}

Adduser-success.jsp

<!DOCTYPE html>
<html>
<head>
<meta http-euiv="Content-Type" content="text/html";charset=ISO-8859-1">
<title>Add User Success</title>
</head>
<body>
<p> Record successfully saved!</p>
<jsp:include page="userform.html"></jsp:include>
</body>
</html>

Adduser-error.jsp

<!DOCTYPE html>
<html>
<head>
<meta http-euiv="Content-Type" content="text/html";charset=ISO-8859-1">
<title>Add User Error</title>
</head>
<body>
<p>Sorry, an error occurred!</p>
<jsp:include page="userform.html"></jsp:include>
</body>
</html>

Viewusers.jsp

<!DOCTYPE html>
<html>
<head>
<meta http-euiv="Content-Type" content="text/html";charset=ISO-8859-1">
<title>View Users</title>
</head>
<body>
<%@page import="com.javapoint.dao.Userdao,com.javapoint.bean.*.java.util.*"%>
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>

<h1>Users List</h1>
<%
List<User> list=UserDao.getAllRecords();
request.setAttribute("list",list);
%>

<table border="1" width="90%">
<tr><th>Id</th><th>Name</th><th>Password</th><th>Email</th><th>Sex</th><th>Country</th><th>Edit</th><th>Delete</th></tr>
<c:forEach items="${list}" var="u">
<tr><td>${u.getId()}</td><td>${u.getName()}</td><td>${u.getPassword()}</td><td>${u.getEmail()}</td><td>${u.getSex()}</td><td>${u.getCountry()}</td>
<td><a href="editform.jsp?id=$u.getId()}">Edit</a></td> 
<td><a href="deleteuser.jsp?id=$u.getId()}">Delete</a></td></tr>
</c:forEach>
</table>
<br/><a href="adduserform.jsp">Add New User</a>
</body>
</html>

Editform.jsp

<!DOCTYPE html>
<html>
<head>
<meta http-euiv="Content-Type" content="text/html";charset=ISO-8859-1">
<title>Edit Form</title>
</head>
<body>
<%@page import="com.javapoint.dao.Userdao,com.javapoint.bean.*.java.util.*"%>

<%
String id=request.getParamater("id");
User u=UserDao.getRecordById(Intege.parseInt(id));
%>
<h1>Edit Form</h1>
<form action="edituser.jsp" method="post">
<input type="hidden" name="id" value="<%=u.getId()%>"/>
<table>
<tr><td>Name:</td><td><input type="text" name="name" value="<%=u.getName()%>/></td></tr>
<tr><td>Password:</td><td><input type="password" name="password"value="<%=u.getPassword()%>/></td></tr>
<tr><td>Email:</td><td><input type='"email" name="email" value="<%=u.getEmail()%>/></td></tr>
<tr><td>Sex:</td><td>
<input type="radio" name="sex" value"male"/>Male
<input type="radio" name="sex" value"female"/>Female</td></tr>
<tr><td>Country:</td><td>
<select name='country' style='width:150px'>
<option>India</option>
<option>Pakistan</option>
<option>Afghanistan</option>
<option>Berma</option>
<option>Other</option>
</select>
</td></tr>
<tr><td colspan='2'><input type="submit" value="Add User"/></td></tr>
</table>
</form>
</body>
</html>

Edituser.jsp
<%@page import="com.javapoint.dao.UserDao"%>
<jsp:useBean id="u" class="com.javapoint.bean.User"></jsp:useBean>
<jsp:setProperty property="*" name="u"/>
<%
int i=UserDao.save(u);
response.sendRedirect("viewusrs.jsp");
%>

Deleteuser.jsp

<%@page import="com.javapoint.dao.UserDao"%>
<jsp:useBean id="u" class="com.javapoint.bean.User"></jsp:useBean>
<jsp:setProperty property="*" name="u"/>

<%
UserDao.delete(u);
response.sendRedirect("viewusers.jsp");
%>


'''
"""
