import { Routes } from '@angular/router';
import { SignInComponent } from './pages/sign-in/sign-in.component';
import { SignUpComponent } from './pages/sign-up/sign-up.component';
import { InventoryComponent } from './pages/inventory/inventory.component';
import { InventoryAddPageComponent } from './pages/inventory-add-page/inventory-add-page.component';
import { InventoryUpdatePageComponent } from './pages/inventory-update-page/inventory-update-page.component';

export const routes: Routes = [
    { path: '', component: SignInComponent},
    { path: 'sign-up', component: SignUpComponent},
    { path: 'inventory', component: InventoryComponent},
    { path: 'inventory-add', component: InventoryAddPageComponent},
    { path: 'inventory-update/:id', component: InventoryUpdatePageComponent},
];
