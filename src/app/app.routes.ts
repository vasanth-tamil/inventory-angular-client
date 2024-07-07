import { Routes } from '@angular/router';
import { SignInComponent } from './pages/sign-in/sign-in.component';
import { SignUpComponent } from './pages/sign-up/sign-up.component';
import { InventoryComponent } from './pages/inventory/inventory.component';

export const routes: Routes = [
    { path: '', component: SignInComponent},
    { path: 'sign-up', component: SignUpComponent},
    { path: 'inventory', component: InventoryComponent},
];
