import { Component } from '@angular/core';
import { InventoryInterface } from '../inventory/inventory.interface';
import { HttpClient } from '@angular/common/http';
import { ApiConstant } from '../../../constants/api-contants';

@Component({
  selector: 'app-inventory-update-page',
  standalone: true,
  imports: [],
  templateUrl: './inventory-update-page.component.html',
  styleUrl: './inventory-update-page.component.css'
})
export class InventoryUpdatePageComponent {

  constructor(private http: HttpClient) { }


  ngOnInit() {
    this.onFetch();
  }


  // inventory data list
  inventoryData: InventoryInterface = {
    ID: 0,
    category: '',
    date_added: '',
    item_name: '',
    last_update: '',
    location: '',
    quantity: 0,
    reorderd_level: 0,
    supplier: '',
    unit_price: 0
  }

  // fetch inventory list
  onFetch() {
    const id: number = 1;
    this.http.get<InventoryInterface>(`${ApiConstant.inventory}/${id}`).subscribe((data) => {
      this.inventoryData = data;
    });
  }

  // delete inventory
  onUpdate(id: number) {
    this.http.put(`${ApiConstant.inventory}/${id}`, this.inventoryData).subscribe((data) => {
      console.log("Updated Successfully");
    })
  }
}
