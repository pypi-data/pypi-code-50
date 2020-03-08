Ans="""
'''

Student.java
import java .io.Serializable;
public class Student
{
private String sname;
private int rno, marks;

public Student()
{
sname="";
}
public void setSname(String name)
{
sname = name;
}
public String getSname()
{
return sname;
}
public void setRno(int r)
{
rno = r;
}
public intgetRno()
{
return rno;
}
public void setMarks(int m)
{
marks = m;
}
public intgetMarks()
{
return marks;
}
} 

Hello.jsp

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title> WELCOME TO STUDENT INFORMATION </title>
</head>
<jsp:useBean id="stud" class="Student" scope="reuest"/>
<jsp:setProperty name="stud" property="sname" value="Shreeji"/>
<jsp:setProperty name="stud" property="rno" value="52"/>
<jsp:setProperty name="stud" property="marks" value="95"/>
<body>
<h1>Name of Student is:<jsp:setProperty name="stud" property="sname"/></h1> 
<h1>Roll No of Student is:<jsp:setProperty name="stud" property="rno"/></h1>
<h1>Marks of Student is:<jsp:setProperty name="stud" property="marks"/></h1>
</body>
</html>


'''
"""
