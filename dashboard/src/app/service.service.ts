import { Injectable } from '@angular/core';
import { Http } from '@angular/http';

@Injectable({
  providedIn: 'root'
})
export class ServiceService {

   constructor(public http: Http){

  }
  search(value){
    return this.http.get(`http://localhost:5000/get_records/${value}`).toPromise()
  }
  search_all(){
    return this.http.get(`http://localhost:5000/get_all_records`).toPromise()
  }
  post_record(data){
    return this.http.post(`http://localhost:5000/add_record`, data).toPromise()
  }
}
