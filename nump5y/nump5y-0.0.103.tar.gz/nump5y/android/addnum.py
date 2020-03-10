Ans="""

<?xml version="1.0" encoding="utf-8"?> 
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity"
    tools:layout_editor_absoluteY="81dp"> 
  
    <!-- Text view for result view-->
    <TextView
        android:id="@+id/textView_answer"
        android:layout_width="100dp"
        android:layout_height="25dp"
        android:layout_marginLeft="130dp"
        android:layout_marginTop="300dp"
        android:text="0"
        android:textSize="20dp"
        android:textStyle="bold" /> 
  
    <!--take the input first number-->
    <EditText
        android:id="@+id/editText_first_no"
        android:layout_width="150dp"
        android:layout_height="40dp"
        android:layout_marginLeft="200dp"
        android:layout_marginTop="40dp"
        android:inputType="number" /> 
    <!-- for messege input first number-->
    <TextView
        android:id="@+id/textView_first_no"
        android:layout_width="150dp"
        android:layout_height="25dp"
        android:layout_marginLeft="10dp"
        android:layout_marginTop="50dp"
        android:text="First number"
        android:textSize="20dp" /> 
  
    <!--view messege -->
    <TextView
        android:id="@+id/textView_second_no"
        android:layout_width="150dp"
        android:layout_height="25dp"
        android:layout_marginLeft="10dp"
        android:layout_marginTop="100dp"
        android:text="Second number"
        android:textSize="20dp" /> 
  
    <!-- take input for second number -->
  
    <EditText
        android:id="@+id/editText_second_no"
        android:layout_width="150dp"
        android:layout_height="40dp"
        android:layout_marginLeft="200dp"
        android:layout_marginTop="90dp"
        android:inputType="number"
        tools:ignore="MissingConstraints" /> 
  
    <!-- button for run add logic and view result -->
  
    <Button
        android:id="@+id/add_button"
        android:layout_width="100dp"
        android:layout_height="50dp"
        android:layout_marginLeft="110dp"
        android:layout_marginTop="200dp"
        android:text="ADD" /> 
  
</RelativeLayout> 

package org.geeksforgeeks.addtwonumbers; 
  
import android.support.v7.app.AppCompatActivity; 
import android.os.Bundle; 
import android.view.View; 
import android.widget.Button; 
import android.widget.EditText; 
import android.widget.TextView; 
  
public class MainActivity extends AppCompatActivity { 
  
    // define the global variable 
  
    // variable number1, number2 for input input number 
    // Add_button, result textView 
  
    EditText number1; 
    EditText number2; 
    Button Add_button; 
    TextView result; 
    int ans=0; 
  
    @Override
    protected void onCreate(Bundle savedInstanceState) { 
        super.onCreate(savedInstanceState); 
        setContentView(R.layout.activity_main); 
  
        // by ID we can use each component which id is assign in xml file 
        number1=(EditText) findViewById(R.id.editText_first_no); 
        number2=(EditText) findViewById(R.id.editText_second_no); 
        Add_button=(Button) findViewById(R.id.add_button); 
        result = (TextView) findViewById(R.id.textView_answer); 
  
        // Add_button add clicklistener 
        Add_button.setOnClickListener(new View.OnClickListener() { 
  
            public void onClick(View v) { 
  
                // num1 or num2 double type 
                // get data which is in edittext, convert it to string 
                // using parse Double convert it to Double type 
                double num1 = Double.parseDouble(number1.getText().toString()); 
                double num2 = Double.parseDouble(number2.getText().toString()); 
                // add both number and store it to sum 
                double sum = num1 + num2; 
                // set it ot result textview 
                result.setText(Double.toString(sum)); 
            } 
        }); 
    } 
} 
"""
