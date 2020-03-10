Ans="""

Following is the content of the modified main activity file src/com.example.demo/MainActivity.java. This file can include each of the fundamental lifecycle methods.

package com.example.demo;

import android.os.Bundle;
import android.app.Activity;

public class MainActivity extends Activity {
   @Override
   protected void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
      setContentView(R.layout.activity_main);
   }
   
}

Following will be the content of res/layout/activity_main.xml file −

<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
   android:layout_width="fill_parent"
   android:layout_height="fill_parent"
   android:paddingLeft="16dp"
   android:paddingRight="16dp" >
   
   <EditText
      android:id="@+id/name"
      android:layout_width="fill_parent"
      android:layout_height="wrap_content"
      android:hint="@string/reminder" />
      
   <LinearLayout
      android:orientation="vertical"
      android:layout_width="fill_parent"
      android:layout_height="fill_parent"
      android:layout_alignParentStart="true"
      android:layout_below="@+id/name">
      
      <Button
         android:layout_width="wrap_content"
         android:layout_height="wrap_content"
         android:text="New Button"
         android:id="@+id/button" />
      
      <Button
         android:layout_width="wrap_content"
         android:layout_height="wrap_content"
         android:text="New Button"
         android:id="@+id/button2" />
      
   </LinearLayout>

</RelativeLayout>

Following will be the content of res/values/strings.xml to define two new constants −

<?xml version="1.0" encoding="utf-8"?>
<resources>
   <string name="action_settings">Settings</string>
   <string name="reminder">Enter your name</string>
</resources>

"""
