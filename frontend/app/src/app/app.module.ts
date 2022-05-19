import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';

import { ConfigService } from './services/config.service';
import { ContextService } from './services/context.service';
import { ApiService } from './services/api.service';

import { ParentExampleComponent } from './parent-example/parent-example.component';

@NgModule({
  declarations: [
    AppComponent,
    ParentExampleComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
  ],
  providers: [
    ConfigService,
    ContextService,
    ApiService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
