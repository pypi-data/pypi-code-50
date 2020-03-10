Ans="""


Step 1: Creating the Required XML File named 'Countries.xml'.

    <?xml version="1.0" encoding="utf-8" ?>  
    <Countries>  
        <Country>  
            <CountryID>1</CountryID>  
            <CountryName>India</CountryName>  
        </Country>  
        <Country>  
            <CountryID>2</CountryID>  
            <CountryName>USA</CountryName>  
        </Country>  
        <Country>  
            <CountryID>3</CountryID>  
            <CountryName>China</CountryName>  
        </Country>  
        <Country>  
            <CountryID>4</CountryID>  
            <CountryName>Australia</CountryName>  
        </Country>  
        <Country>  
            <CountryID>5</CountryID>  
            <CountryName>United Kingdom</CountryName>  
        </Country>  
        <Country>  
            <CountryID>6</CountryID>  
            <CountryName>Brazil</CountryName>  
        </Country>  
    </Countries>    

Step 2: Drag and Drop a Dropdownlist Control from ASP.NET Controls Toolbox and Press F7 Key to Add the Below code to the Code Behind File.

    using System;    
    using System.Data;    
    using System.Web.UI.WebControls;    
    namespace DDLPopulateWithXML    
    {    
        public partial class WebForm1 : System.Web.UI.Page    
        {    
            protected void Page_Load(object sender, EventArgs e)    
            {    
                if (!IsPostBack) //Used to Check that Whether the page loads first time or Second Time    
                {    
                    DataSet ds = new DataSet(); //Created a Dataset to Store data    
                    ds.ReadXml(Server.MapPath("Countries.xml")); // Using ReadXml Method of the Dataset Class and Server.MapPath is used to  
    Get the Correct path of the XML File    
                    DropDownList1.DataSource = ds; //Setting the Datasource of DDL to Dataset    
                    DropDownList1.DataTextField = "CountryName"; //This is the name of the tag of XML file through which we want to Show the Values    
                    DropDownList1.DataValueField = "CountryID"; //This is the Primary key on which the Data is fetched    
                    DropDownList1.DataBind(); //Data is Binded with the dropdownlist    
                    ListItem LI = new ListItem("---Select---", "-1"); //Used to Show Some Custom Text in the list of DDL    
                    DropDownList1.Items.Insert(0,LI); //Used to Insert the Above Value at the 0 Index Location of the DDL, so that It appears  
    on Top    
                }    
            }    
        }    
    } 
        

"""
