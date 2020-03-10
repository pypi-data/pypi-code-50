Ans="""

string myName = "myName is Shreesh";  
       myName = myName.ToUpper();  
       Console.WriteLine(myName);

myName = myName.ToLower();  
Console.WriteLine(myName);

       myName = myName.Trim();  
Console.WriteLine(myName);

       bool  isContains = myName.Contains("SHREESH");  
       Console.WriteLine(isContains);

char[] charArray = myName.ToCharArray();  
foreach(char c in charArray)  
      {  
    Console.WriteLine(c);  
}

string myName = "myName is SHREESH";  
         myName =  myName.Substring(0, 6);  
    Console.WriteLine(myName);

"""
