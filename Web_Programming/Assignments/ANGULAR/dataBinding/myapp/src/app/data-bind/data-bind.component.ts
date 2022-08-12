import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-data-bind',
  templateUrl: './data-bind.component.html',
  styleUrls: ['./data-bind.component.css']
})
export class DataBindComponent implements OnInit {

  username = ""
  contact:any = {}
  /*myImg:string = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F758223287267043932%2F&psig=AOvVaw0E25-x5uxf2yuphrxhciFe&ust=1651569986923000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCLCCkua_wPcCFQAAAAAdAAAAABAJ"
  myTxt:string = "Payal Button"
  myDefValue:string = "Some defualt value"    // variables created for data binding
  flag:boolean = true*/
  constructor() { 
    this.username="Payal"
    this.contact={mail:"test.com",phone:1234567890}
  }
  getname()
  {
    return this.username
  }

  ngOnInit(): void {
  }

}
