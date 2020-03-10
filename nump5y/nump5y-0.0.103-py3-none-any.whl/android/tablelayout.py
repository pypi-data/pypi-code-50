Ans="""

Following is the content of the modified main activity file src/com.example.demo/MainActivity.java. This file can include each of the fundamental lifecycle methods.

package com.example.demo;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;

public class MainActivity extends Activity {
   @Override
   protected void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
      setContentView(R.layout.activity_main);
   }
   
}

Following will be the content of res/layout/activity_main.xml file −

<TableLayout xmlns:android="http://schemas.android.com/apk/res/android"
   android:layout_width="fill_parent"
   android:layout_height="fill_parent">
   
   <TableRow
      android:layout_width="fill_parent"
      android:layout_height="fill_parent">
		
      <TextView
         android:text="Time"
         android:layout_width="wrap_content"
         android:layout_height="wrap_content"
         android:layout_column="1" />
			
      <TextClock
         android:layout_width="wrap_content"
         android:layout_height="wrap_content"
         android:id="@+id/textClock"
         android:layout_column="2" />
			
   </TableRow>
   
   <TableRow>
	
      <TextView
         android:text="First Name"
         android:layout_width="wrap_content"
         android:layout_height="wrap_content"
         android:layout_column="1" />
			
      <EditText
         android:width="200px"
         android:layout_width="wrap_content"
         android:layout_height="wrap_content" />
   </TableRow>
   
   <TableRow>
	
      <TextView
         android:text="Last Name"
         android:layout_width="wrap_content"
         android:layout_height="wrap_content"
         android:layout_column="1" />
			
      <EditText
         android:width="100px"
         android:layout_width="wrap_content"
         android:layout_height="wrap_content" />
   </TableRow>
   
   <TableRow
      android:layout_width="fill_parent"
      android:layout_height="fill_parent">
		
      <RatingBar
         android:layout_width="wrap_content"
         android:layout_height="wrap_content"
         android:id="@+id/ratingBar"
         android:layout_column="2" />
   </TableRow>
   
   <TableRow
      android:layout_width="fill_parent"
      android:layout_height="fill_parent"/>
		
   <TableRow
      android:layout_width="fill_parent"
      android:layout_height="fill_parent">
		
      <Button
         android:layout_width="wrap_content"
         android:layout_height="wrap_content"
         android:text="Submit"
         android:id="@+id/button"
         android:layout_column="2" />
   </TableRow>

</TableLayout>

Following will be the content of res/values/strings.xml to define two new constants −

<?xml version="1.0" encoding="utf-8"?>
<resources>
   <string name="app_name">HelloWorld</string>
   <string name="action_settings">Settings</string>
</resources>

"""
