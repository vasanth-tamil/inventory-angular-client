import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component } from '@angular/core';
import { InventoryInterface } from '../../../types/inventory.interface';
import { ApiConstant } from '../../../constants/api-contants';
import { AuthHelper } from '../../../utils/auth_helper';
import { FormControl, FormGroup, NgModel, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { NgToastModule, NgToastService } from 'ng-angular-popup';

@Component({
  selector: 'app-inventory',
  standalone: true,
  imports: [NgToastModule],
  templateUrl: './inventory.component.html',
  styleUrl: './inventory.component.css'
})
export class InventoryComponent {

  constructor(private http: HttpClient, private router: Router, private toast: NgToastService) { }

  // inventory data list
  inventoryList: InventoryInterface[] = [];

  ngOnInit() {
    if (!AuthHelper.isAuthenticated()) {
      this.router.navigate(['/']);
    }

    this.onFetch();
  }

  onLogout() {
    AuthHelper.removeToken()
    this.toast.success("Logout Successfully", '', 2000);
    this.router.navigate(['/']);
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
        this.toast.success("Inventory Limit Set Successfully", '', 2000);
        this.onFetch();
    })
  }

  // delete inventory
  onDelete(id: number) {
    const barearHeader = AuthHelper.getBarearHeader();
    this.http.delete(`${ApiConstant.inventory}/${id}`, {headers: barearHeader as any}).subscribe((data) => {
      this.toast.success("Inventory Deleted Successfully", '', 2000);
      this.onFetch();
    })
  }
}
