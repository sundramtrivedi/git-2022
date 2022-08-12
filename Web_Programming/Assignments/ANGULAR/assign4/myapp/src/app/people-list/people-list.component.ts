import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-people-list',
  templateUrl: './people-list.component.html',
  styleUrls: ['./people-list.component.css']
})
export class PeopleListComponent {

  orderid:string=''
  custname:string=''
  billingdate:string=''
  shippingdate:string=''
  ordertotal:string=''
  constructor() 
  { 
    
  }

  

}
