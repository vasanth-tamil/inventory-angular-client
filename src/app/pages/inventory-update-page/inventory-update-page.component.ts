import { NgFor } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormControl, FormGroup, FormsModule, NgForm, ReactiveFormsModule, Validators } from '@angular/forms';
import { AuthHelper } from '../../../utils/auth_helper';
import { ApiConstant } from '../../../constants/api-contants';
import { Response } from '../../../types/response.type';
import { InventoryInterface } from '../../../types/inventory.interface';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-inventory-update-page',
  standalone: true,
  imports: [NgFor, FormsModule, ReactiveFormsModule],
  templateUrl: './inventory-update-page.component.html',
  styleUrl: './inventory-update-page.component.css'
})
export class InventoryUpdatePageComponent {

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

  inventoryUpdateForm: FormGroup = new FormGroup({
    item_name: new FormControl('', [Validators.required]),
    category: new FormControl('Electronics', [Validators.required]),
    quantity: new FormControl('', [Validators.required]),
    unit_price: new FormControl('', [Validators.required]),
    supplier: new FormControl('', [Validators.required]),
    location: new FormControl('', [Validators.required]),
    warning_limit: new FormControl('5'),
  });

  constructor(private http: HttpClient, private activatedRoute: ActivatedRoute) { }
  
  ngOnInit(): void {
    const id = Number(this.activatedRoute.snapshot.paramMap.get('id'));
    this.http.get<InventoryInterface>(`${ApiConstant.inventory}/${id}`).subscribe((data) => {
      this.inventoryUpdateForm = new FormGroup({
        item_name: new FormControl(data.item_name, [Validators.required]),
        category: new FormControl(data.category, [Validators.required]),
        quantity: new FormControl(data.quantity.toString(), [Validators.required]),
        unit_price: new FormControl(data.unit_price.toString(), [Validators.required]),
        supplier: new FormControl(data.supplier, [Validators.required]),
        location: new FormControl(data.location, [Validators.required]),
        warning_limit: new FormControl(data.warning_limit),
      });
    })
  }

  // update inventory
  updateInventory() {
    const id = Number(this.activatedRoute.snapshot.paramMap.get('id'));
    const barearHeader = AuthHelper.getBarearHeader();
    const requestData: any = this.inventoryUpdateForm.value;

    if (this.inventoryUpdateForm.valid) {
      console.log(requestData.quantity, requestData.warning_limit)
      // check limit
      if (requestData.quantity < requestData.warning_limit) {
        alert("limit error");
      }

      console.log(requestData);
      this.http.put<Response>(`${ApiConstant.inventory}/${id}`, requestData, {headers: barearHeader as any}).subscribe((data) => {
        console.log(data); 
      });
    }

  }
}
