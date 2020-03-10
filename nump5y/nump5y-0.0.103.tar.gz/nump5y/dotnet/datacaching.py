Ans="""

Using Data Caching
The most important object in caching mechanism is cache object. The Cache object is the fundamental object for all caching in the ASP.NET Framework.

The cache object can be accessed in every page of your application. It works same as Session object. Storing and retrieving the object in cache is very easy.

Cache["Key"]="Item";

Normally you store database object in Cache, so it will reduce the database calling again and again.

Some of the important methods of Cache object are as follows:

    Add: It adds a new item to the cache.
    Get: It returns a particular item from the cache.
    Insert: It is used to insert a new item into the cache. This method replaces the already exists item.
    Remove: This method is used to remove an item from the cache.

Cache is a powerful object, you can add into it DataSet, DataTable, ArrayList etc.

Now let’s take an example and create a web application in which we will take two web pages. In first page, we will add the dataset object into the cache and then access this cached data from second page.

FirstPage.aspx.cs

using System;
using System.Configuration;
using System.Data;
using System.Data.SqlClient;
public partial class FirstPage : System.Web.UI.Page
{
    SqlConnection conn;
    SqlDataAdapter adapter;
    DataSet ds;
    
    string cs = ConfigurationManager.ConnectionStrings["conString"].ConnectionString;
    protected void Page_Load(object sender, EventArgs e)
    {
        ds=new DataSet();
        conn = new SqlConnection(cs);
        adapter = new SqlDataAdapter("select * from tblEmps", conn);      
        adapter.Fill(ds);
        Cache["Data"] = ds;       
    }
    
    protected void Button1_Click(object sender, EventArgs e)
    {
        Response.Redirect("SecondPage.aspx");
    }
}

Now you can use Cache["Data"] object in any web page of your application. Cache returns the Object type, therefore you must typecast to underlying data type.

SecondPage.aspx.cs

using System;
using System.Data;
public partial class SecondPage : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        DataSet ds=(DataSet)Cache["Data"];
        GridView1.DataSource = ds;
        GridView1.DataBind();
    }
}

Adding Items to the Cache
Insert() method is used to add items to the cache. Insert() method have several overloaded method. Insert method can accept following parameters in different version of overloaded method.

    Key: It specifies the name of the new item.
    Value: It specifies the value of the new item.
    Dependencies: It supports the file, key, or SQL dependency. You can apply any of dependencies at a time.
    absoluteExpiration: DataTime object is used to specify the time duration. It is used to specify an absolute expiration time for the cached data. After that data is removed automatically from the cache.
    slidingExpiration: DataSpan object is used to specify the time duration. It is used to specify a sliding expiration duration for the cached data.
    Priority: It is used to set the priority of the cached item. You can use any of the following value  AboveNormal, BelowNormal, Default, High, Low, Normal, and NotRemovable.

Adding Items with an Expiration Policy
You can add different data object in cache object. When the memory is going to full, the server will automatically remove the item from cache. You can also specify an expiration time when the item will remove from the cache.

We can add the object into the cache by using insert() method. The cache.insert() method has 4 overloaded methods.


There are two different ways to expire the cache on the basis of time.

1. Absolute Expiration
2. Sliding Expiration

Absolute Expiration: This policy is useful when you know that your data does not change frequently. As its name suggests, the data from the cache will be removed after specified time, irrespective of whether cached data is accessed from cache or not. In absolute expiration DataTime object is used to specify the time duration.

Example

string strData = "The string data to be cached";        
Cache.Insert("AbsoluteCacheKey", strData, null,
DateTime.Now.AddMinutes(1), System.Web.Caching.Cache.NoSlidingExpiration);

Sliding Expiration: It defines that how long the data should remain available in the cache after the data was last accessed. It keeps the most frequently accessed items in memory. In sliding expiration TimeSpan object is used to specify the time duration.

Example

Cache.Insert("SlidingExpiration", strData, null,
System.Web.Caching.Cache.NoAbsoluteExpiration, TimeSpan.FromMinutes(1));

In the above examples, we have used string data type for caching, but you can use DataSet, DataTable, ArrayList or other type of data.
We cannot use absolute expiration and sliding expiration policies simultaneously. If you try to do it, it will give you runtime error.

Cache dependency on files
Suppose that we have data in a file and this data is cached for some specified time duration. If you want that whenever the file data is modified, the cached data is automatically removed from the cache. For this to happen we need to provide a dependency on the file.
First we will add a XML file in our project and write data as given below.

<?xml version="1.0" encoding="utf-8" ?>
<EmployeeInfo>
     <Employee>
          <EmpID>1</EmpID>
          <Name>Raj</Name>
          <Address>Pune</Address>
     </Employee>
     <Employee>
          <EmpID>2</EmpID>
          <Name>Shiva</Name>
          <Address>USA</Address>
     </Employee>
     <Employee>
          <EmpID>3</EmpID>
          <Name>Digvijay</Name>
          <Address>NewYork</Address>
     </Employee>
</EmployeeInfo>

Now take a GridView, a button, and a label on the web page and write code for access the EmployeeInfo.xml file.

using System;
using System.Data;
using System.Web.Caching;
public partial class DepandencyDemo : System.Web.UI.Page
{    
    protected void Page_Load(object sender, EventArgs e)
    {         
    }    
    protected void btnGetEmp_Click(object sender, EventArgs e)
    {
        if (Cache["EmpData"] != null)
        {
            DataSet ds = (DataSet)Cache["EmpData"];
            GridView1.DataSource = ds;
            GridView1.DataBind();
            Label1.Text = ds.Tables[0].Rows.Count.ToString()+"  records are retrieved from cache";
        }
        else
        {
            DataSet ds = new DataSet();
            ds.ReadXml(MapPath("∼/EmployeeInfo.xml"));
            Cache.Insert("EmpData", ds, new CacheDependency(MapPath("∼/EmployeeInfo.xml")), DateTime.Now.AddMinutes(1) Cache.NoSlidingExpiration);
            GridView1.DataSource = ds;
            GridView1.DataBind();
            Label1.Text = ds.Tables[0].Rows.Count.ToString() + "  records are retrieved from EmployeeInfo.xml file";
        }
    }
}

"""
