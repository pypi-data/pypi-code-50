Ans="""

Step 2 − Add the following code to res/layout/activity_main.xml.

<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
   xmlns:tools="http://schemas.android.com/tools"
   android:layout_width="match_parent"
   android:layout_height="match_parent"
   tools:context=".MainActivity">
   <TextView
      android:id="@+id/textView"
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:layout_centerInParent="true"
      android:text="Click button below to bring up snackBar" />
   <Button
      android:id="@+id/callbackButton"
      android:layout_width="wrap_content"
      android:layout_height="wrap_content"
      android:layout_centerInParent="true"
      android:layout_below="@id/textView"
      android:layout_marginTop="16sp"
      android:text="Tap To Display SnackBar"
      android:textStyle="bold"
      android:textSize="16sp"/>
</RelativeLayout>

Step 3 – Open build.gradle(Module app) add the following dependancy -

implementation 'com.android.support:design:28.0.0'

Step 4 − Add the following code to src/MainActivity.java

import android.graphics.Color;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
public class MainActivity extends AppCompatActivity {
   @Override
   protected void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
      setContentView(R.layout.activity_main);
      Button button = findViewById(R.id.callbackButton);
      button.setOnClickListener(new View.OnClickListener() {
         public void onClick(View v) {
            Snackbar snackBar = Snackbar .make(v, "An Error Occurred!", Snackbar.LENGTH_LONG) .setAction("RETRY", new View.OnClickListener() {
               @Override
               public void onClick(View view) {
               }
            });
            snackBar.setActionTextColor(Color.BLUE);
            View snackBarView = snackBar.getView();
            TextView textView = snackBarView.findViewById(android.support.design.R.id.snackbar_text);
            textView.setTextColor(Color.RED);
            snackBar.show();
         }
      });
   }
}

Step 4 - Add the following code to androidManifest.xml

<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android" package="app.com.sample">
   <application
      android:allowBackup="true"
      android:icon="@mipmap/ic_launcher"
      android:label="@string/app_name"
      android:roundIcon="@mipmap/ic_launcher_round"
      android:supportsRtl="true"
      android:theme="@style/AppTheme">
      <activity android:name=".MainActivity">
         <intent-filter>
            <action android:name="android.intent.action.MAIN" />
            <category android:name="android.intent.category.LAUNCHER" />
         </intent-filter>
      </activity>
   </application>
</manifest>
 
"""
