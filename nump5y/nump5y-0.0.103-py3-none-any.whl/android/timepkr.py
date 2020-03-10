Ans="""

    <?xml version="1.0" encoding="utf-8"?>  
    <RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"  
        xmlns:app="http://schemas.android.com/apk/res-auto"  
        xmlns:tools="http://schemas.android.com/tools"  
        android:layout_width="match_parent"  
        android:layout_height="match_parent"  
        tools:context="example.javatpoint.com.timepicker.MainActivity">  
      
        <TextView  
            android:id="@+id/textView1"  
            android:layout_width="wrap_content"  
            android:layout_height="wrap_content"  
            android:layout_above="@+id/button1"  
            android:layout_alignParentLeft="true"  
            android:layout_alignParentStart="true"  
            android:layout_marginBottom="102dp"  
            android:layout_marginLeft="30dp"  
            android:layout_marginStart="30dp"  
            android:text="" />  
      
        <Button  
            android:id="@+id/button1"  
            android:layout_width="wrap_content"  
            android:layout_height="wrap_content"  
            android:layout_alignParentBottom="true"  
            android:layout_centerHorizontal="true"  
            android:layout_marginBottom="20dp"  
            android:text="Change Time" />  
      
        <TimePicker  
            android:id="@+id/timePicker"  
            android:layout_width="wrap_content"  
            android:layout_height="wrap_content"  
            android:layout_above="@+id/textView1"  
            android:layout_centerHorizontal="true"  
            android:layout_marginBottom="36dp" />  
    </RelativeLayout>  

Activity class
File: MainActivity.java

    package example.javatpoint.com.timepicker;  
      
    import android.support.v7.app.AppCompatActivity;  
    import android.os.Bundle;  
    import android.view.View;  
    import android.widget.Button;  
    import android.widget.TextView;  
    import android.widget.TimePicker;  
      
    public class MainActivity extends AppCompatActivity {  
        TextView textview1;  
        TimePicker timepicker;  
        Button changetime;  
        @Override  
        protected void onCreate(Bundle savedInstanceState) {  
            super.onCreate(savedInstanceState);  
            setContentView(R.layout.activity_main);  
      
            textview1=(TextView)findViewById(R.id.textView1);  
            timepicker=(TimePicker)findViewById(R.id.timePicker);  
            //Uncomment the below line of code for 24 hour view  
            timepicker.setIs24HourView(true);  
            changetime=(Button)findViewById(R.id.button1);  
      
            textview1.setText(getCurrentTime());  
      
            changetime.setOnClickListener(new View.OnClickListener(){  
                @Override  
                public void onClick(View view) {  
                    textview1.setText(getCurrentTime());  
                }  
            });  
      
        }  
      
        public String getCurrentTime(){  
            String currentTime="Current Time: "+timepicker.getCurrentHour()+":"+timepicker.getCurrentMinute();  
            return currentTime;  
        }  
      
    } 
    
"""
