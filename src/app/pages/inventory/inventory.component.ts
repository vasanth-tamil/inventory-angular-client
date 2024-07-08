import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component } from '@angular/core';
import { InventoryInterface } from '../../../types/inventory.interface';
import { ApiConstant } from '../../../constants/api-contants';
import { AuthHelper } from '../../../utils/auth_helper';
import { FormControl, FormGroup, NgModel, Validators } from '@angular/forms';

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

  onSetLimit(event: any, id: number) {
    event.preventDefault();
    const requestLimitData = { limit: event.target.limit.value };
    const barearHeader = AuthHelper.getBarearHeader();
    this.http.post(`${ApiConstant.inventory}/set-limit/${id}`, requestLimitData, {headers: barearHeader as any}).subscribe((data) => {
      console.log(data);
    })
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
