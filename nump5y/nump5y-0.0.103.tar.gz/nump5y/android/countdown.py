Ans="""

Step 1 − Create a new project in Android Studio, go to File ⇒ New Project and fill all required details to create a new project.

Step 2 − Add the following code to res/layout/activity_main.xml.

<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
   android:layout_width="match_parent"
   android:id="@+id/layout"
   android:gravity="center"
   android:layout_height="match_parent"
   android:orientation="vertical">
   <TextView
      android:id="@+id/counttime"
      android:layout_width="match_parent"
      android:gravity="center"
      android:textSize="30sp"
      android:layout_height="wrap_content" />
</LinearLayout>

In the above code, we have declared a text view. it going to print countdown timer.

Step 3 − Add the following code to src/MainActivity.java

package com.example.andy.myapplication;
import android.annotation.TargetApi;
import android.os.Build;
import android.os.Bundle;
import android.os.CountDownTimer;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.RatingBar;
import android.widget.TextView;
import android.widget.Toast;
public class MainActivity extends AppCompatActivity {
   public int counter;
   @TargetApi(Build.VERSION_CODES.O)
   @Override
   protected void onCreate(Bundle savedInstanceState) {
      super.onCreate(savedInstanceState);
      setContentView(R.layout.activity_main);
      final TextView counttime=findViewById(R.id.counttime);
      new CountDownTimer(50000,1000) {
         @Override
         public void onTick(long millisUntilFinished) {
            counttime.setText(String.valueOf(counter));
            counter++;
         }
         @Override
         public void onFinish() {
            counttime.setText("Finished");
         }
      }.start();
   }
}
    
"""
