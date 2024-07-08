import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component } from '@angular/core';
import { InventoryInterface } from './inventory.interface';
import { ApiConstant } from '../../../constants/api-contants';
import { AuthHelper } from '../../../utils/auth_helper';

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
    const barearHeader = AuthHelper.getBarearHeader();
    this.http.get<InventoryInterface[]>(ApiConstant.inventory, {headers: barearHeader as any}).subscribe((data) => {
      this.inventoryList = data;
    });
  }

  // delete inventory
  onDelete(id: number) {
    const barearHeader = AuthHelper.getBarearHeader();
    this.http.delete(`${ApiConstant.inventory}/${id}`, {headers: barearHeader as any}).subscribe((data) => {
      console.log("Deleted Successfully");
      this.onFetch();
    })
  }
}
