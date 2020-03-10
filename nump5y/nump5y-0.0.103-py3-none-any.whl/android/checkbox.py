Ans="""

    <?xml version="1.0" encoding="utf-8"?>  
    <android.support.constraint.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"  
        xmlns:app="http://schemas.android.com/apk/res-auto"  
        xmlns:tools="http://schemas.android.com/tools"  
        android:layout_width="match_parent"  
        android:layout_height="match_parent"  
        tools:context="example.javatpoint.com.checkbox.MainActivity">  
      
      
        <CheckBox  
            android:id="@+id/checkBox"  
            android:layout_width="wrap_content"  
            android:layout_height="wrap_content"  
            android:layout_marginLeft="144dp"  
            android:layout_marginTop="68dp"  
            android:text="Pizza"  
            app:layout_constraintStart_toStartOf="parent"  
            app:layout_constraintTop_toTopOf="parent" />  
      
        <CheckBox  
            android:id="@+id/checkBox2"  
            android:layout_width="wrap_content"  
            android:layout_height="wrap_content"  
            android:layout_marginLeft="144dp"  
            android:layout_marginTop="28dp"  
            android:text="Coffee"  
            app:layout_constraintStart_toStartOf="parent"  
            app:layout_constraintTop_toBottomOf="@+id/checkBox" />  
      
        <CheckBox  
            android:id="@+id/checkBox3"  
            android:layout_width="wrap_content"  
            android:layout_height="wrap_content"  
            android:layout_marginLeft="144dp"  
            android:layout_marginTop="28dp"  
            android:text="Burger"  
            app:layout_constraintStart_toStartOf="parent"  
            app:layout_constraintTop_toBottomOf="@+id/checkBox2" />  
      
        <Button  
            android:id="@+id/button"  
            android:layout_width="wrap_content"  
            android:layout_height="wrap_content"  
            android:layout_marginLeft="144dp"  
            android:layout_marginTop="184dp"  
            android:text="Order"  
            app:layout_constraintStart_toStartOf="parent"  
            app:layout_constraintTop_toBottomOf="@+id/checkBox3" />  
      
    </android.support.constraint.ConstraintLayout>  

Activity class

Let's write the code to check which toggle button is ON/OFF.
File: MainActivity.java

    package example.javatpoint.com.checkbox;  
      
    import android.support.v7.app.AppCompatActivity;  
    import android.os.Bundle;  
    import android.view.View;  
    import android.widget.Button;  
    import android.widget.CheckBox;  
    import android.widget.Toast;  
      
    public class MainActivity extends AppCompatActivity {  
        CheckBox pizza,coffe,burger;  
        Button buttonOrder;  
        @Override  
        protected void onCreate(Bundle savedInstanceState) {  
            super.onCreate(savedInstanceState);  
            setContentView(R.layout.activity_main);  
            addListenerOnButtonClick();  
        }  
        public void addListenerOnButtonClick(){  
            //Getting instance of CheckBoxes and Button from the activty_main.xml file  
            pizza=(CheckBox)findViewById(R.id.checkBox);  
            coffe=(CheckBox)findViewById(R.id.checkBox2);  
            burger=(CheckBox)findViewById(R.id.checkBox3);  
            buttonOrder=(Button)findViewById(R.id.button);  
      
            //Applying the Listener on the Button click  
            buttonOrder.setOnClickListener(new View.OnClickListener(){  
      
                @Override  
                public void onClick(View view) {  
                    int totalamount=0;  
                    StringBuilder result=new StringBuilder();  
                    result.append("Selected Items:");  
                    if(pizza.isChecked()){  
                        result.append("\nPizza 100Rs");  
                        totalamount+=100;  
                    }  
                    if(coffe.isChecked()){  
                        result.append("\nCoffe 50Rs");  
                        totalamount+=50;  
                    }  
                    if(burger.isChecked()){  
                        result.append("\nBurger 120Rs");  
                        totalamount+=120;  
                    }  
                    result.append("\nTotal: "+totalamount+"Rs");  
                    //Displaying the message on the toast  
                    Toast.makeText(getApplicationContext(), result.toString(), Toast.LENGTH_LONG).show();  
                }  
      
            });  
        }  
    }

    
"""
