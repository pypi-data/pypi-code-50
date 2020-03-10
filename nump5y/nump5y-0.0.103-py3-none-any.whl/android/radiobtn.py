Ans="""

activity_main.xml

File: activity_main.xml

    <?xml version="1.0" encoding="utf-8"?>  
    <LinearLayout  
        xmlns:android="http://schemas.android.com/apk/res/android"  
        xmlns:tools="http://schemas.android.com/tools"  
        android:layout_width="match_parent"  
        android:layout_height="match_parent"  
        android:orientation="vertical"  
        tools:context="example.javatpoint.com.radiobutton.MainActivity">  
      
        <TextView  
            android:id="@+id/textView1"  
            android:layout_width="fill_parent"  
            android:layout_height="wrap_content"  
            android:layout_marginTop="30dp"  
            android:gravity="center_horizontal"  
            android:textSize="22dp"  
            android:text="Single Radio Buttons" />  
      
      
      
        <!--   Default RadioButtons  -->  
      
        <RadioButton  
            android:id="@+id/radioButton1"  
            android:layout_width="fill_parent"  
            android:layout_height="wrap_content"  
            android:layout_gravity="center_horizontal"  
            android:text="Radio Button 1"  
            android:layout_marginTop="20dp"  
      
            android:textSize="20dp" />  
        <RadioButton  
            android:id="@+id/radioButton2"  
            android:layout_width="fill_parent"  
            android:layout_height="wrap_content"  
            android:text="Radio Button 2"  
            android:layout_marginTop="10dp"  
      
            android:textSize="20dp" />  
      
      
        <View  
            android:layout_width="fill_parent"  
            android:layout_height="1dp"  
            android:layout_marginTop="20dp"  
            android:background="#B8B894" />  
      
        <TextView  
            android:id="@+id/textView2"  
            android:layout_width="fill_parent"  
            android:layout_height="wrap_content"  
            android:layout_marginTop="30dp"  
            android:gravity="center_horizontal"  
            android:textSize="22dp"  
            android:text="Radio button inside RadioGroup" />  
      
      
        <!--   Customized RadioButtons  -->  
      
      
        <RadioGroup  
            android:layout_width="wrap_content"  
            android:layout_height="wrap_content"  
            android:id="@+id/radioGroup">  
      
            <RadioButton  
                android:id="@+id/radioMale"  
                android:layout_width="fill_parent"  
                android:layout_height="wrap_content"  
                android:text="  Male"  
                android:layout_marginTop="10dp"  
                android:checked="false"  
                android:textSize="20dp" />  
      
            <RadioButton  
                android:id="@+id/radioFemale"  
                android:layout_width="fill_parent"  
                android:layout_height="wrap_content"  
                android:text="   Female"  
                android:layout_marginTop="20dp"  
                android:checked="false"  
      
                android:textSize="20dp" />  
        </RadioGroup>  
      
        <Button  
            android:layout_width="wrap_content"  
            android:layout_height="wrap_content"  
            android:text="Show Selected"  
            android:id="@+id/button"  
            android:onClick="onclickbuttonMethod"  
            android:layout_gravity="center_horizontal" />  
      
      
    </LinearLayout>  

Activity class

File: MainActivity.java

    package example.javatpoint.com.radiobutton;  
      
    import android.support.v7.app.AppCompatActivity;  
    import android.os.Bundle;  
    import android.view.View;  
    import android.widget.Button;  
    import android.widget.RadioButton;  
    import android.widget.RadioGroup;  
    import android.widget.Toast;  
      
    public class MainActivity extends AppCompatActivity {  
        Button button;  
        RadioButton genderradioButton;  
        RadioGroup radioGroup;  
        @Override  
        protected void onCreate(Bundle savedInstanceState) {  
            super.onCreate(savedInstanceState);  
            setContentView(R.layout.activity_main);  
            radioGroup=(RadioGroup)findViewById(R.id.radioGroup);  
        }  
        public void onclickbuttonMethod(View v){  
            int selectedId = radioGroup.getCheckedRadioButtonId();  
            genderradioButton = (RadioButton) findViewById(selectedId);  
            if(selectedId==-1){  
                Toast.makeText(MainActivity.this,"Nothing selected", Toast.LENGTH_SHORT).show();  
            }  
            else{  
                Toast.makeText(MainActivity.this,genderradioButton.getText(), Toast.LENGTH_SHORT).show();  
            }  
      
        }  
    }  
"""
