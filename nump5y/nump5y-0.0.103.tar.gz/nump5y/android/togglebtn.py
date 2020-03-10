Ans="""

    <?xml version="1.0" encoding="utf-8"?>  
    <android.support.constraint.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"  
        xmlns:app="http://schemas.android.com/apk/res-auto"  
        xmlns:tools="http://schemas.android.com/tools"  
        android:layout_width="match_parent"  
        android:layout_height="match_parent"  
        tools:context="example.javatpoint.com.togglebutton.MainActivity">  
      
        <ToggleButton  
            android:id="@+id/toggleButton"  
            android:layout_width="wrap_content"  
            android:layout_height="wrap_content"  
            android:layout_marginLeft="8dp"  
            android:layout_marginTop="80dp"  
            android:text="ToggleButton"  
            android:textOff="Off"  
            android:textOn="On"  
            app:layout_constraintEnd_toStartOf="@+id/toggleButton2"  
            app:layout_constraintStart_toStartOf="parent"  
            app:layout_constraintTop_toTopOf="parent" />  
      
        <ToggleButton  
            android:id="@+id/toggleButton2"  
            android:layout_width="wrap_content"  
            android:layout_height="wrap_content"  
            android:layout_marginRight="60dp"  
            android:layout_marginTop="80dp"  
            android:text="ToggleButton"  
            android:textOff="Off"  
            android:textOn="On"  
            app:layout_constraintEnd_toEndOf="parent"  
            app:layout_constraintTop_toTopOf="parent" />  
      
        <Button  
            android:id="@+id/button"  
            android:layout_width="wrap_content"  
            android:layout_height="wrap_content"  
            android:layout_marginBottom="144dp"  
            android:layout_marginLeft="148dp"  
            android:text="Submit"  
            app:layout_constraintBottom_toBottomOf="parent"  
            app:layout_constraintStart_toStartOf="parent" />  
    </android.support.constraint.ConstraintLayout>  

Activity class

Let's write the code to check which toggle button is ON/OFF.
File: MainActivity.java

    package example.javatpoint.com.togglebutton;  
      
    import android.support.v7.app.AppCompatActivity;  
    import android.os.Bundle;  
    import android.view.View;  
    import android.widget.Button;  
    import android.widget.Toast;  
    import android.widget.ToggleButton;  
      
    public class MainActivity extends AppCompatActivity {  
        private ToggleButton toggleButton1, toggleButton2;  
        private Button buttonSubmit;  
        @Override  
        protected void onCreate(Bundle savedInstanceState) {  
            super.onCreate(savedInstanceState);  
            setContentView(R.layout.activity_main);  
      
            addListenerOnButtonClick();  
        }  
      
        public void addListenerOnButtonClick(){  
            //Getting the ToggleButton and Button instance from the layout xml file  
            toggleButton1=(ToggleButton)findViewById(R.id.toggleButton);  
            toggleButton2=(ToggleButton)findViewById(R.id.toggleButton2);  
            buttonSubmit=(Button)findViewById(R.id.button);  
      
            //Performing action on button click  
            buttonSubmit.setOnClickListener(new View.OnClickListener(){  
      
                @Override  
                public void onClick(View view) {  
                    StringBuilder result = new StringBuilder();  
                    result.append("ToggleButton1 : ").append(toggleButton1.getText());  
                    result.append("\nToggleButton2 : ").append(toggleButton2.getText());  
                    //Displaying the message in toast  
                    Toast.makeText(getApplicationContext(), result.toString(),Toast.LENGTH_LONG).show();  
                }  
      
            });  
      
        }  
    }
    
"""
