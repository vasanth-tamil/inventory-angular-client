import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { InventoryInterface } from './inventory.interface';
import { ApiConstant } from '../../../constants/api-contants';

@Component({
  selector: 'app-inventory',
  standalone: true,
  imports: [],
  templateUrl: './inventory.component.html',
  styleUrl: './inventory.component.css'
})
export class InventoryComponent {

  constructor(private http: HttpClient) { }

  // inventory data list
  inventoryList: InventoryInterface[] = [];

  ngOnInit() {
    this.onFetch();
  }

  // fetch inventory list
  onFetch() {
    this.http.get<InventoryInterface[]>(ApiConstant.inventory).subscribe((data) => {
      this.inventoryList = data;
    });
  }

  // delete inventory
  onDelete(id: number) {
    this.http.delete(`${ApiConstant.inventory}/${id}`).subscribe((data) => {
      console.log("Deleted Successfully");
      this.onFetch();
    })
  }
}
