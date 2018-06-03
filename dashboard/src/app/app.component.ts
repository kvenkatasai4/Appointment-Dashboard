import { Component } from '@angular/core';
import { ServiceService } from './service.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  isData: boolean;
  isAlertBox: boolean;
  form_error:string;
  data;
  isTable: boolean;
  settings;
  isTableAlertBox:boolean;
  table_error:string;
  success:boolean;
  constructor(public service: ServiceService){

  }
  ngOnInit() {
    this.isData = false;
    this.isAlertBox = false;
    this.form_error = "";
    this.isTable = false;
    this.table_error = "";
    this.isTableAlertBox = false;
    this.success = false;
  }
  validate() {
    this.success = false;
    this.isAlertBox =false;
    if (this.isData == true)
      this.isData = false;
    else
    this.isData = true;
  }
  search(value){
    if (value){
      this.service.search(value).then((response) => {
      this.data = response.json();
      this.isTable = true;
      this.success = false;
    }).catch((err) => {
      this.isTableAlertBox = true;
      this.table_error = "Response Error"
      this.success = false;
    });
    }
    else{
      this.service.search_all().then((response) => {
      this.data = response.json()
      this.isTable = true
      this.success = false;
    }).catch((err) => {
      this.isTableAlertBox = true;
      this.table_error = "Response Error"
      this.success = false;
    });
    }
  }
  submit(date: Date, time:string, description:string){
    if (!date || !time || !description){
      this.isAlertBox =true;
      this.success = false;
      this.form_error = "Invalid form";
    }
    else{
      this.isAlertBox = false;
      var currentdate = new Date()
      if( parseInt(date.toString().split("-")[2]) < currentdate.getDate() ||
        parseInt(date.toString().split("-")[1]) < (currentdate.getMonth() + 1) ||
        parseInt(date.toString().split("-")[0]) < currentdate.getFullYear()){
          this.isAlertBox =true;
          this.form_error = "Invalid Date";
      }else{
        this.service.post_record({'description':description, 'time':time, 'date': date}).then((response) => {
          if (response.json() == true){
            this.success = true;
            }
          }).catch((err) => {
            this.isAlertBox = true;
            this.form_error = "Response Error"
          });
      }
    }
  }
}
