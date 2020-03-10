Ans="""

    <?xml version="1.0" encoding="utf-8"?>  
    <android.support.constraint.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"  
        xmlns:app="http://schemas.android.com/apk/res-auto"  
        xmlns:tools="http://schemas.android.com/tools"  
        android:layout_width="match_parent"  
        android:layout_height="match_parent"  
        tools:context="example.javatpoint.com.screenorientation.MainActivity">  
      
      
        <Button  
            android:id="@+id/button1"  
            android:layout_width="wrap_content"  
            android:layout_height="wrap_content"  
            android:layout_marginBottom="8dp"  
            android:layout_marginTop="112dp"  
            android:onClick="onClick"  
            android:text="Launch next activity"  
            app:layout_constraintBottom_toBottomOf="parent"  
            app:layout_constraintEnd_toEndOf="parent"  
            app:layout_constraintHorizontal_bias="0.612"  
            app:layout_constraintStart_toStartOf="parent"  
            app:layout_constraintTop_toBottomOf="@+id/editText1"  
            app:layout_constraintVertical_bias="0.613" />  
      
        <TextView  
            android:id="@+id/editText1"  
            android:layout_width="wrap_content"  
            android:layout_height="wrap_content"  
            android:layout_centerHorizontal="true"  
            android:layout_marginEnd="8dp"  
            android:layout_marginStart="8dp"  
            android:layout_marginTop="124dp"  
            android:ems="10"  
            android:textSize="22dp"  
            android:text="This activity is portrait orientation"  
            app:layout_constraintEnd_toEndOf="parent"  
            app:layout_constraintHorizontal_bias="0.502"  
            app:layout_constraintStart_toStartOf="parent"  
            app:layout_constraintTop_toTopOf="parent" />  
    </android.support.constraint.ConstraintLayout>  

Activity class
File: MainActivity.java

    package example.javatpoint.com.screenorientation;  
      
    import android.content.Intent;  
    import android.support.v7.app.AppCompatActivity;  
    import android.os.Bundle;  
    import android.view.View;  
    import android.widget.Button;  
      
    public class MainActivity extends AppCompatActivity {  
      
        Button button1;  
        @Override  
        protected void onCreate(Bundle savedInstanceState) {  
            super.onCreate(savedInstanceState);  
            setContentView(R.layout.activity_main);  
      
            button1=(Button)findViewById(R.id.button1);  
        }  
        public void onClick(View v) {  
            Intent intent = new Intent(MainActivity.this,SecondActivity.class);  
            startActivity(intent);  
        }  
    }  

activity_second.xml
File: activity_second.xml

    <?xml version="1.0" encoding="utf-8"?>  
    <android.support.constraint.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"  
        xmlns:app="http://schemas.android.com/apk/res-auto"  
        xmlns:tools="http://schemas.android.com/tools"  
        android:layout_width="match_parent"  
        android:layout_height="match_parent"  
        tools:context="example.javatpoint.com.screenorientation.SecondActivity">  
      
        <TextView  
            android:id="@+id/textView"  
            android:layout_width="wrap_content"  
            android:layout_height="wrap_content"  
            android:layout_marginEnd="8dp"  
            android:layout_marginStart="8dp"  
            android:layout_marginTop="180dp"  
            android:text="this is landscape orientation"  
            android:textSize="22dp"  
            app:layout_constraintEnd_toEndOf="parent"  
            app:layout_constraintHorizontal_bias="0.502"  
            app:layout_constraintStart_toStartOf="parent"  
            app:layout_constraintTop_toTopOf="parent" />  
    </android.support.constraint.ConstraintLayout>  

SecondActivity class
File: SecondActivity.java

    package example.javatpoint.com.screenorientation;  
      
    import android.support.v7.app.AppCompatActivity;  
    import android.os.Bundle;  
      
    public class SecondActivity extends AppCompatActivity {  
      
        @Override  
        protected void onCreate(Bundle savedInstanceState) {  
            super.onCreate(savedInstanceState);  
            setContentView(R.layout.activity_second);  
      
        }  
    }  

AndroidManifest.xml
File: AndroidManifest.xml

In AndroidManifest.xml file add the screenOrientation attribute in activity and provides its orientation. In this example, we provide "portrait" orientation for MainActivity and "landscape" for SecondActivity.

    <?xml version="1.0" encoding="utf-8"?>  
    <manifest xmlns:android="http://schemas.android.com/apk/res/android"  
        package="example.javatpoint.com.screenorientation">  
      
        <application  
            android:allowBackup="true"  
            android:icon="@mipmap/ic_launcher"  
            android:label="@string/app_name"  
            android:roundIcon="@mipmap/ic_launcher_round"  
            android:supportsRtl="true"  
            android:theme="@style/AppTheme">  
            <activity  
                android:name="example.javatpoint.com.screenorientation.MainActivity"  
                android:screenOrientation="portrait">  
                <intent-filter>  
                    <action android:name="android.intent.action.MAIN" />  
      
                    <category android:name="android.intent.category.LAUNCHER" />  
                </intent-filter>  
            </activity>  
            <activity android:name=".SecondActivity"  
                android:screenOrientation="landscape">  
            </activity>  
        </application>  
      
    </manifest>

"""
