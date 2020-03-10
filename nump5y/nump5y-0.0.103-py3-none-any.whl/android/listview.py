Ans="""

package com.example.ListDisplay;

import android.os.Bundle;
import android.app.Activity;
import android.view.Menu;
import android.widget.ArrayAdapter;
import android.widget.ListView;

public class ListDisplay extends Activity {
   // Array of strings...
   String[] mobileArray = {"Android","IPhone","WindowsMobile","Blackberry",
      "WebOS","Ubuntu","Windows7","Max OS X"};
   
   @Override
   protected void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
      setContentView(R.layout.activity_main);
      
      ArrayAdapter adapter = new ArrayAdapter<String>(this, 
         R.layout.activity_listview, mobileArray);
      
      ListView listView = (ListView) findViewById(R.id.mobile_list);
      listView.setAdapter(adapter);
   }
}

Following will be the content of res/layout/activity_main.xml file −

<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
   xmlns:tools="http://schemas.android.com/tools"
   android:layout_width="match_parent"
   android:layout_height="match_parent"
   android:orientation="vertical"
   tools:context=".ListActivity" >

   <ListView
      android:id="@+id/mobile_list"
      android:layout_width="match_parent"
      android:layout_height="wrap_content" >
   </ListView>
 
</LinearLayout>

Following will be the content of res/values/strings.xml to define two new constants −

<?xml version="1.0" encoding="utf-8"?>
<resources>
   <string name="app_name">ListDisplay</string>
   <string name="action_settings">Settings</string>
</resources>

Following will be the content of res/layout/activity_listview.xml file −

<?xml version="1.0" encoding="utf-8"?>
<!--  Single List Item Design -->

<TextView xmlns:android="http://schemas.android.com/apk/res/android"
   android:id="@+id/label"
   android:layout_width="fill_parent"
   android:layout_height="fill_parent"
   android:padding="10dip"
   android:textSize="16dip"
   android:textStyle="bold" >
</TextView>
    
"""
