Ans="""
'''

import java.sql.*;
import java.io.*;
 
public class DatabaseImageExample {
	public static void main(String args[]){
		try{
			Class.forName("com.mysql.jdbc.Driver");
			Connection con=DriverManager.getConnection("jdbc:mysql://localhost/demo","root","root");
			
			File file=new File("E:\\image.png");
			FileInputStream fis=new FileInputStream(file);
			
			PreparedStatement ps=con.prepareStatement("insert into image_table (name,image) values(?,?)"); 
			ps.setString(1,"image 1");
			ps.setBinaryStream(2,fis,(int)file.length());
			ps.executeUpdate();
 
			ps.close();
			fis.close();
			con.close();
		}catch(Exception e){
			e.printStackTrace();
		}
	}
}

'''
"""
