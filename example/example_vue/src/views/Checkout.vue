<template>
  <div class="page-checkout">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Checkout</h1>
      </div>

      <div class="column is-12 box">
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>Product</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in cart.items" :key="item.product.id">
              <td>{{ item.product.name }}</td>
              <td>{{ item.product.price }}</td>
              <td>{{ item.quantity }}</td>
              <td>{{ getITemTotal(item).toFixed(2) }}</td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="column is-12 box">
        <h2 class="subtitle">Shiping details</h2>
        <p class="has-text-grey mb-4">* All fields are required</p>
        <div class="columns is-multiline">
          <div class="column is-6">
            <div class="field">
              <label>First name*</label>
              <div class="control">
                <input type="text" class="input" v-model="first_name" />
              </div>
            </div>
            <div class="field">
              <label>Last name*</label>
              <div class="control">
                <input type="text" class="input" v-model="last_name" />
              </div>
            </div>
            <div class="field">
              <label>E-mail*</label>
              <div class="control">
                <input type="email" class="input" v-model="email" />
              </div>
            </div>
            <div class="field">
              <label>Phone*</label>
              <div class="control">
                <input type="tel" class="input" v-model="phone" />
              </div>
            </div>
          </div>
          <div class="column is-6">
            <div class="field">
              <label>Address*</label>
              <div class="control">
                <input type="tel" class="input" v-model="address" />
              </div>
            </div>
            <div class="field">
              <label>ZIP code*</label>
              <div class="control">
                <input type="tel" class="input" v-model="zipcode" />
              </div>
            </div>
            <div class="field">
              <label>Place*</label>
              <div class="control">
                <input type="tel" class="input" v-model="place" />
              </div>
            </div>
          </div>

        </div>
        <div class="notification is-danger" v-if="errors.length">
        <p v-for="error in errors" :key="error">{{ error }}</p>
        </div>
        <hr>
        <div class="mb-5" id="cart-element">
        </div>
        <template>
            <hr>
            <button class="button is-dark" @click="submitForm">Pay with Stripe</button>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Checkout",
  data() {
    return {
      cart: {
        items: [],
      },
      stripe: {},
      card: {},
      first_name: "",
      last_name: "",
      email: "",
      phone: "",
      address: "",
      zipcode: "",
      place: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Checkout | EXAMPLE";

    this.cart = this.$store.getters.cart;
  },
  methods: {
    getITemTotal(item) {
      return item.quantity * item.product.price;
    },
    submitForm() {
        this.errors = []
        if (this.first_name === '') {
            this.errors.push('First Name is missing')
        }
        if (this.last_name === '') {
            this.errors.push('Last Name is missing')
        }
        if (this.email === '') {
            this.errors.push('Email is missing')
        }
        if (this.phone === '') {
            this.errors.push('Phone is missing')
        }
        if (this.address === '') {
            this.errors.push('Address is missing')
        }
        if (this.zipcode === '') {
            this.errors.push('ZIP code is missing')
        }
        if (this.place === '') {
            this.errors.push('Place is missing')
        }
    }
  },
  computed: {
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.product.price * curVal.quantity);
      }, 0);
    },
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return (acc += curVal.quantity);
      }, 0);
    },
  },
};
</script>
