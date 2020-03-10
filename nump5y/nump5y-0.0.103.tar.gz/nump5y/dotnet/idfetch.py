Ans="""



    SqlConnection nwindConn = new SqlConnection("Data Source=localhost;Integrated Security=SSPI;Initial Catalog=northwind");  
    SqlCommand selectCMD = new SqlCommand("SELECT CustomerID, CompanyName FROM Customers", nwindConn);  
    selectCMD.CommandTimeout = 30;  
    SqlDataAdapter customerDA = new SqlDataAdapter();  
    customerDA.SelectCommand = selectCMD;  
    nwindConn.Open();  
    DataSet customerDS = new DataSet();  
    customerDA.Fill(customerDS, "Customers");  
    nwindConn.Close();  


        

"""
