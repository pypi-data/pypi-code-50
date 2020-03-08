Ans="""
'''

Follow the steps:
1.Download the jar from here-
https://code.google.com/archive/p/json-simple/downloads.
2.Gotonetbeans- in your “Projects” window go for- “libraries” right click on it and “json-simple-1.1.1” folder to it.
3.Write encoding code:

import java.util.HashMap;
import java.util.Map;
import org.json.simple.JSONValue;

public class JSON_USING_MAP
{
public static void main(String args[])
{
Map obj = new HashMap()
System.out.println("Encoding Using MAP....\n");

obj.put("COLLEGE NAME","ABC COLLEGE");
obj.put("YEAR OF ESTD",new Integer(1927));
obj.put("NO OF COURSES",new Double(60));

String txt = JSONValue.to.JSONString(obj);
System.out.print(txt);
}
}
4.This will generate certain output.
Encoding….
{“NO OF COURSES”:60.0,”YEAR OF ESTD”:1927,”COLLEGE NAME”:”XYZ COLLEGE”}
 
5.We can also obtain same results using MAP.

import org.json.simple.JSONObject;
public class JSON_ENCODE_DECODE
{
public static void main(String[] args)
{
JSONObject obj = new JSONObject();
System.out.println("Encoding.....\n");

obj.put("COLLEGE NAME","ABC COLLEGE");
obj.put("YEAR OF ESTD",new Integer(1927));
obj.put("NO OF COURSES",new Double(60));

System.out.print(obj);
}
}

6.This will also generate certain output.
Encoding Using MAP…..
{“NO OF COURSES”:60.0,”YEAR OF ESTD”:1927,”COLLEGE NAME”:”XYZ COLLEGE”}

7.Let’s see how to decode…

import org.json.simple.JSONObject;
import org.json.simple.JSONValue;

public class JSON_DECODE
{
public static void main(String[] args)
{
String s="{\"COLLEGE NAME\":\"XYZ COLLEGE\",\"YEAR OF ESTD\":1987.0,\"NO OF COURSES\":56}";
Object obj = JSONValue.parse(s);

JSONObject Obj = (JSONObject) obj;

String col_name = (String)jsObj.get("COLLEGE NAME");
double year = (Double)jsObj.get("YEAR OF ESTD");
long courses = (Long)jsObj.get("NO OF COURSES");
System.out.println(col_name+"\n"+year+"\n"+courses);
}
}

8.This will generate following output:
XYZ COLLEGE
1987.0
56 

'''
"""
