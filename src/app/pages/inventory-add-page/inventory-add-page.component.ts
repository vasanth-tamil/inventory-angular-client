import { NgFor } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormControl, FormGroup, FormsModule, NgForm, ReactiveFormsModule, Validators } from '@angular/forms';
import { AuthHelper } from '../../../utils/auth_helper';
import { ApiConstant } from '../../../constants/api-contants';
import { Response } from '../../../types/response.type';
import { InventoryInterface } from '../../../types/inventory.interface';
import { NgToastModule, NgToastService } from 'ng-angular-popup';
import { Router } from '@angular/router';

@Component({
  selector: 'app-inventory-add-page',
  standalone: true,
  imports: [NgFor, FormsModule, ReactiveFormsModule, NgToastModule],
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

  inventoryAddForm = new FormGroup({
    item_name: new FormControl('', [Validators.required]),
    category: new FormControl('Electronics', [Validators.required]),
    quantity: new FormControl('', [Validators.required]),
    unit_price: new FormControl('', [Validators.required]),
    supplier: new FormControl('', [Validators.required]),
    location: new FormControl('', [Validators.required]),
  });

  constructor(private http: HttpClient, private router: Router, private toast: NgToastService) { }

  ngOnInit(): void {
    if (!AuthHelper.isAuthenticated()) {
      this.router.navigate(['/']);
    }
  }

  // fetch inventory list
  addInventory() {
    this.inventoryAddForm.markAllAsTouched();

    console.log(this.inventoryAddForm.value)
 
    if (this.inventoryAddForm.valid) {
      const barearHeader = AuthHelper.getBarearHeader();
      const requestData: any = this.inventoryAddForm.value;
      this.http.post<Response>(ApiConstant.inventory, requestData, {headers: barearHeader as any}).subscribe((data) => {
        
        this.toast.success("Inventory Added Successfully", '', 2000);
        this.router.navigate(['inventory']);
        this.inventoryAddForm.reset();
      });
    }

  }
}
