Ans="""


using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;
namespace IUDS_SimpleCS
{
public partial class Form1 : Form
{
public Form1()
{
InitializeComponent();
}
SqlConnection con = new SqlConnection(@"Data Source=.\sqlexpress;Initial Catalog=Employee;Integrated Security=True");
 
 
private void btnAdd_Click(object sender, EventArgs e)
{
try
{
if (txtEmpName.Text == "" || txtEmpDegn.Text == "" || txtSalary.Text == "")
{
MessageBox.Show("All Fields Are Compulsory");
}
else
{
SqlCommand cmdinsert = new SqlCommand("Insert into EmployeeDetails values( ' " + txtEmpName.Text + " ','" + txtEmpDegn.Text + "','" + txtSalary.Text + "' )", con);
con.Open();
cmdinsert.CommandType = CommandType.Text;
cmdinsert.ExecuteNonQuery();
MessageBox.Show("Data Inserted");
}
}
catch (Exception ex)
{
MessageBox.Show(ex.Message);
}
finally
{
if (con.State == ConnectionState.Open)
{
con.Close();
}
}
}
 
private void btnUpdate_Click(object sender, EventArgs e)
{
try
{
if (txtempid.Text == "")
{
MessageBox.Show("Enter Employee Id To Update");
}
else
{
SqlCommand cmdupdate = new SqlCommand("Update EmployeeDetails SET EmpName='" + txtEmpName.Text + "',EmpDesgn='" + txtEmpDegn.Text + "' ,EmpSalary='" + txtSalary.Text + "' where EmpId=" + txtempid.Text + "", con);
con.Open();
cmdupdate.CommandType = CommandType.Text;
cmdupdate.ExecuteNonQuery();
MessageBox.Show("Data Updated");
}
}
catch (Exception ex)
{
MessageBox.Show(ex.Message);
}
finally
{
if (con.State == ConnectionState.Open)
{
con.Close();
}
}
}
 
private void btnDel_Click(object sender, EventArgs e)
{
try
{
if (txtempid.Text == "")
{
MessageBox.Show("Enter Employee Id To Delete");
}
else
{
SqlCommand cmddel = new SqlCommand("Delete EmployeeDetails where EmpId=" + txtempid.Text + "", con);
con.Open();
cmddel.CommandType = CommandType.Text;
cmddel.ExecuteNonQuery();
MessageBox.Show("Data Deleted");
}
}
catch (Exception ex)
{
MessageBox.Show(ex.Message);
}
finally
{
if (con.State == ConnectionState.Open)
{
con.Close();
}
}
}
 
 
 
private void btnSelect_Click(object sender, EventArgs e)
{
try
{
if (txtempid.Text == "")
{
MessageBox.Show("Enter Employee Id To Search");
}
else
{
SqlCommand cmd = new SqlCommand("Select * From EmployeeDetails where EmpId=" + txtempid.Text + "", con);
con.Open();
 
cmd.CommandType = CommandType.Text;
SqlDataReader dr = cmd.ExecuteReader();
if (dr.Read())
{
txtEmpName.Text = dr[1].ToString();
txtEmpDegn.Text = dr[2].ToString();
txtSalary.Text = dr[3].ToString();
}
dr.Close();
}
}
catch (Exception ex)
{
MessageBox.Show(ex.Message);
}
finally
{
if (con.State == ConnectionState.Open)
{
con.Close();
}
}
}
 
private void btnReset_Click(object sender, EventArgs e)
{
foreach (Control T in Controls)
{
if (T is TextBox)
{
T.Text = "";
}
}
}
}
}

        

"""
