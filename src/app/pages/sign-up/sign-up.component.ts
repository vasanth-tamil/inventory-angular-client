import { Component } from '@angular/core';
import { FormControl, FormGroup, FormsModule, NgForm, NgModel, ReactiveFormsModule, Validators } from '@angular/forms';
import { User } from '../../../types/user.type';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { ApiConstant } from '../../../constants/api-contants';
import { Router } from '@angular/router';
import { NgToastModule, NgToastService } from 'ng-angular-popup';

@Component({
  selector: 'app-sign-up',
  standalone: true,
  imports: [FormsModule, CommonModule, ReactiveFormsModule, NgToastModule],
  templateUrl: './sign-up.component.html',
  styleUrl: './sign-up.component.css'
})
export class SignUpComponent {
  
  signUpForm = new FormGroup({
    email: new FormControl('', [Validators.required, Validators.email]),
    password: new FormControl('', [Validators.required]),
    re_password: new FormControl('', [Validators.required]),
  });

  constructor(private http: HttpClient, private router: Router, private toast: NgToastService) { }

  onSignUp() {
    this.signUpForm.markAllAsTouched();

    if(this.signUpForm.valid) {
      this.http.post(ApiConstant.signUp, this.signUpForm.value).subscribe((data) => {
        this.toast.success("Sign Up Successfully", '', 2000);
        this.router.navigate(['/']);

        this.signUpForm.reset();
      });
    }
  }

}
