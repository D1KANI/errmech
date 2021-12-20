<template>
    <tr>
        <td>
            <router-link :to="item.product.get_absolute_url">
                {{ item.product.name }}
            </router-link>
        </td>
        <td>
            ${{ item.product.price }}
        </td>
        <td>
            <a @click="decrementQuantity(item)">-</a>
            {{ item.quantity }}
            <a @click="incrementQuantity(item)">+</a>
        </td>
        <td>
            ${{ getItemTotal(item).toFixed(2) }}
        </td>
        <td>
            <button @click="removeFromCart(item)" class="delete"></button>
        </td>
    </tr>
</template>

<script>
import { getters } from "vuex"


export default ({
    name: 'CartItem',
    props: {
        initialItem: Object
    },
    data() {
        return {
            item: this.initialItem
        }
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price;
        },
        decrementQuantity(item) {
            item.quantity -= 1;
            if (item.quantity === 0) {
                this.$emit('removeFromCart', item)
            }
            this.updateCart();
        },
        incrementQuantity(item) {
            item.quantity += 1;
            this.updateCart();
        },
        updateCart() {
            localStorage.setItem('cart', JSON.stringify(this.$store.getters.cart))
        },
        removeFromCart(item) {
            this.$emit('removeFromCart', item)
            this.updateCart();
        }
    }
})
</script>
