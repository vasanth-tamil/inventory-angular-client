import { NgFor } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-inventory-add-page',
  standalone: true,
  imports: [NgFor],
  templateUrl: './inventory-add-page.component.html',
  styleUrl: './inventory-add-page.component.css'
})
export class InventoryAddPageComponent {

  protected inventoryCategories: string[] = [
    "Electronics",
    "Furniture",
    "Groceries",
    "Clothing",
    "Books",
    "Toys",
    "Office Supplies",
    "Sports Equipment",
    "Beauty Products",
    "Automotive Parts"
  ];

  constructor(http: HttpClient) { }


  protected addInventory() {
    console.log(this)
  }

}
