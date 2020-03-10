Ans="""

protected void Page_Load(object sender, EventArgs e)
    {

    }
    protected void btnclear_Click(object sender, EventArgs e)
    {
        ViewState["name"] = txtname.Text;
        txtname.Text = "";
    }
    protected void btndisplay_Click(object sender, EventArgs e)
    {
        lbl.Text = ViewState["name"].ToString();
    }
        

"""
