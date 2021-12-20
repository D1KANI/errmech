<template>
    <div class="column is-2">
        <div class="box">
            <figure class="image mb-4">
                <img :src="product.get_thumbnail" alt="Image Not Found">
            </figure>
            <h3 class="is-size-4">{{ product.name }}</h3>
            <p class="is-size-6 has-gray-text">${{ product.price }}</p>
            <router-link :to="product.get_absolute_url" class="button is-dark mt-4">View Details</router-link>
        </div>
    </div>
</template>

<script>

export default({
    name: 'ProductBox',
    props: {
        product: Object
    }
})
</script>

<style scoped lang="scss">
  .image {
    // margin: -1.25rem -1.25rem 0 -1.25rem;
    user-select: none;
    pointer-events: none;
  }
</style>
