Ans="""
'''

Index.html

<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title> Insert title here </title>
</head>
<body>
<h1> Add New Employee </h1>
<form action="SaveServlet" method="post">
<table>
<tr><td>Name:</td><td><input type="password" name="password"/></td></tr> 
<tr><td>Password:</td><td><input type="password" name="password"/></td></tr> 
<tr><td>Email:</td><td><input type="email" name="email"/></td></tr>
<tr><td>Country:</td><td>
<select name="country" style="width:150px">
<option>India</option>
<option>USA</option>
<option>UK</option>
<option>Other</option>
</select>
</td></tr>
<tr><td colspan="2"><input type="submit" value="Save Employee"/></td></tr>
</table>
</form>
<br/>
<a href="ViewServlet">view employees</a>
</body>
</html>

Emp.java

public class Emp
{
private int id;
private String name,password,email,country;
public int getId()
{
return id;
}
public void setId(int id)
{
this.id=id;
}
public String getName()
{
return name;
}
public void setName(String name)
{
this.name=name;
}
public String getPassword()
{
return password;
}
public void setPassword(String password)
{
this.password=passwrord;
}
public string getEmail
{
return email;
}
public void setEmail(String email)
{
this.email=email;
}
public String getCountry()
{
return country;
}
public void setCountry(String country)
{
this.country=country;
}
}

EmpDao.java

import java.util.*;
import java.sql.*;
public class EmpDao
{
public static Connection getConnection()
{
Connection con = null;
try
{
Class.forName("oracle.jdbc.driver.OracleDriver");
con = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:xe","system","oracle");
}
catch(Exception e)
{
System.out.println(e);
}
return con;
}
public static int save(Emp e)
{
int status=0;
try{
Connection con = EmpDao.getConnection();
PreparedStatement ps = con.prepareStatement("insert into Employee(name,password,email,country)values(?,?,?,?)");
ps.setString(1,e.getName());
ps.setString(2,e.getPassword());
ps.setString(3,e.getEmail());
ps.setString(4,e.getCountry());

status = ps.executeUpdate();
con.close();
}
catch(Exception ex)
{
return status;
}
public static int update(Emp e)
{
int status=0;
try
{
Connection con = EmpDao.getConnection();
PreparedStatement ps = con.prepareStatement("update Employee set name=?,password=?,email=?,country=? where id=?");
ps.setString(1,e.getName());
ps.setString(2,e.getPassword());
ps.setString(3,e.getEmail());
ps.setString(4,e.getCountry());
ps.setInt(5,e.getId());

status = ps.executeUpdate();
con.close();
}
catch(Exception ex)
{
ex.printStackTrace();
}
return status;
}
public static int delete(int id)
{
int status=0;
try
{
Connection con = EmpDao.getConnection();
PreparedStatement ps = con.prepareStatement("update Employee set name=?,password=?,email=?,country=? where id=?");

ps.setInt(1,id);

status = ps.executeUpdate();
con.close();
}
catch(Exception ex)
{
ex.printStackTrace();
}
return status;
}
public static Emp getEmployeeById(int id)
{
Emp e = new Emp();
try
{
Connection con = EmpDao.getConnection();
PreparedStatement ps = con.prepareStatement("select * from Employee where id=?");
ps.setInt(1,id);
ResultSet rs = ps.executeQuery();
if(rs.next())
{
e.setId(rs.getInt(1));
e.setName(rs.getString(2));
e.setPassword(rs.getString(3));
e.setEmail(rs.getString(4));
e.setCountry(rs.getString(5));
}
con.close();
}
catch(Exception ex)
{
ex.printStackTrace();
}
return e;
}
public static List<Emp> getAllEmployees()
{
List<Emp> list = new ArrayList<Emp>();
try
{
Connection con = EmpDao.getConnection();
PreparedStatement ps = con.prepareStatement("select * from Employee");
ResultSet rs = ps.executeQuery();
while(rs.next())
{
Emp e = new Emp();
e.setId(rs.getInt(1));
e.setName(rs.getString(2));
e.setPassword(rs.getString(3));
e.setEmail(rs.getString(4));
e.setCountry(rs.getString(5));
list.add(e);
}
con.close();
}
catch(Exception e)
{
e.printStackTrace();
}
return list;
}
}

SaveServlet.java

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.anotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
@WebServlet("/SaveServlet")
public class SaveServlet2 extends HttpServlet
{
protected void doPost(HttpServletRequest request,HttpServletResponse response)throws ServletException,IOException
{
response.setContentType("text/html");
PrintWriter out=response.getWriter();

String name=request.getParameter("name");
String password=request.getParameter("password");
String email=request.getParameter("email"); 
String country=request.getParameter("country"); 

Emp e=new Emp();
e.setName(name);
e.setPassword(password);
e.setEmail(email);
e.setCountry(country);

int status=EmpDao.save(e);
if(status>0)
{
out.print("<p>Record saved successfully!<p>");
request.getRequestDispatcher("index.html").include(request,response);
}
else
{
out.println("Sorry! unable to save record");
}
out.close();
}
}

EditServlet.java

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
@WebServlet("/EditServlet2")
public class EditServlet2 extends HttpServlet
{
protected void doPost(HttpServletRequest request,HttpServletResponse response)throws ServletException,IOException
{
response.setContentType("text/html");
PrintWriter out=response.getWriter();
out.print("<h1>Update Employee<h1>");
String sid=request.getParameter("id");
int id=Integer.parseInt(sid);

Emp e = EmpDao.getEmployeeById(id);
out.print("<form action='EditServlet2' method='post'>");
out.print("<table>");
out.print("<tr><td></td><td><input type='hidden' name='id' value='"+e.getId()+"'/></td></tr>");
out.print("<tr><td>Name:</td><td><input type='text' name='name' value='"+e.getName()+"'/></td></tr>");
out.print("<tr><td>Password:</td><td><input type='password' name='password' value='"+e.getPassword()+"'/></td></tr>");
out.print("<tr><td>Email:</td><td><input type='email' name='email' value='"+e.getEmail()+"'/></td></tr>");
out.print("<tr><td>Country:</td><td>");
out.print("<select name='country' style='width:150px'>");
out.print("<option>India</option>");
out.print("<option>USA</option>");
out.print("<option>UK</option>");
out.print("<option>Other</option>");
out.print("</select>");
out.print("</td></tr>");
out.print("<tr><td colspan='2'><input type='submit' value='Edit & Save'/></td></tr>");
out.print("</table>");
out.print("</form>");
out.close();
}
}

EditServlet2.java

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
@WebServlet("/EditServlet2")
public class EditServlet2 extends HttpServlet
{
protected void doPost(HttpServletRequest request,HttpServletResponse response)throws ServletException,IOException
{
response.setContentType("text/html");
PrintWriter out=response.getWriter();
String sid=request.getParameter("id");
int id=Integer.parseInt(sid);
String name=request.getParameter("name");
String password=request.getParameter("password");
String email=request.getParameter("email"); 
String country=request.getParameter("country"); 
Emp e=new Emp();
e.setId(id);
e.setName(name);
e.setPassword(password);
e.setEmail(email);
e.setCountry(country);

int status=EmpDao.update(e);
if(status>0)
{
response.sendRedirect("ViewServlet");
}
else
{
out.println("Sorry! unable to update record");
}

out.close();
}
}

DeleteServlet.java

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
@WebServlet("/DeleteServlet2")
public class DeleteServlet2 extends HttpServlet
{
protected void doGet(HttpServletRequest request,HttpServletResponse response)throws ServletException,IOException
{
String sid=request.getParameter("id");
int id=Integer.parseInt(sid);
EmpDao.delete(id);
response.sendRedirect("ViewServlet");
}
}

ViewServlet.java

import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import javax.servlet.ServletException;
importjavax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
@WebServlet("/ViewServlet")
public classViewServlet extends HttpServlet
{
protected void doGet(HttpServletRequest request,HttpServletResponse response)throws ServletException, IOException
{
response.setContentType("text/html");
PrintWriter out=response.getWriter();
out.println("<a href='index.html>Add New Employee</a>");
out.println("<h1>Employees List</h1>");
List<Emp> list=EmpDao.getAllEmployees();

out.print("<table border='1' width='100%'");
out.print("<tr><th>Id</th><th>Nmae</th><th>Password</th><th>Email</th><th>Country</th><th>Edit</th><th>Delete</th></tr>");
for(Emp e:list)
{
out.print("<tr><td>"+e.getId()+"</td><td>"+e.getName()+"</td><td>"+e.getPassword()+"</td><td>"+e.getEmail()+"</td><td>"+e.getCountry()+"</td>
<td><a href='EditServlet?id="+e.getId()+'">edit</a></td>
<td><a href='DeleteServlet?id="+e.getId()+'">delete</a></td></tr>");
}
out.print("</table>");
out.close();
}
}


'''
"""
